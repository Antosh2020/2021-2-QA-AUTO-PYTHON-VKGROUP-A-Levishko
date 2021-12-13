import requests
from urllib.parse import urljoin


class ApiClient:

	def __init__(self, base_url):
		self.base_url = base_url
		self.csrf_token = None
		self.session = requests.Session()

	def post_login(self, user, password):
		location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
		headers = {
			'Content-Type': 'application/x-www-form-urlencoded',
			'Referer': 'https://target.my.com/'}
		data = {
			'email': user,
			'password': password,
			'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
		}
		self.session.post(location, headers=headers, data=data)
		self.csrf_token = self.get_csrf_token()

	def get_csrf_token(self):
		location = '/csrf/'
		url = urljoin(self.base_url, location)
		headers = self.session.get(url).headers['set-cookie'].split(';')
		cookies = [c for c in headers if 'csrftoken' in c]
		csrf_token = cookies[0].split('=')[-1]
		print(csrf_token)
		return csrf_token

	def post_create_segment(self, name, pass_condition, object_type, left=365, right=0, seg_type='positive'):
		location = "/api/v2/remarketing/segments.json?fields=id,name"
		url = urljoin(self.base_url, location)
		headers = {"X-CSRFToken": f'{self.csrf_token}'}
		json = {
			"name": f"{name}",
			"pass_condition": pass_condition,
			"relations": [{"object_type": object_type, "params": {"left": left, "right": right, "type": seg_type}}]}
		response = self.session.post(url, headers=headers, json=json)
		return response

	def post_delete_segment(self, segment_id, source_type='segment'):
		location = "/api/v1/remarketing/mass_action/delete.json"
		url = urljoin(self.base_url, location)
		headers = {"X-CSRFToken": self.csrf_token}
		json = [{"source_id": segment_id, "source_type": source_type}]
		response = self.session.post(url, headers=headers, json=json)
		return response

	def get_check_segment(self, segment_id):
		location = f"/api/v2/remarketing/segments/{segment_id}.json"
		url = urljoin(self.base_url, location)
		response = self.session.get(url=url)
		return response

	def post_upload_image(self, file):
		location = "/api/v2/content/static.json"
		url = urljoin(self.base_url, location)
		image = {'file': open(file, 'rb')}
		headers = {"X-CSRFToken": self.csrf_token}
		response = self.session.post(url=url, headers=headers, files=image)
		return response

	def get_id_url(self, target_url):
		location = f"/api/v1/urls/?url={target_url}"
		url = urljoin(self.base_url, location)
		response = self.session.get(url=url)
		return response

	def get_campaign_status(self, campaign_id):
		location = f"/api/v2/campaigns/{campaign_id}.json?fields=issues"
		url = urljoin(self.base_url, location)
		response = self.session.get(url=url)
		return response

	def post_create_campaign(self, name, image_id, url_id, objective='reach', package_id=960):
		location = "/api/v2/campaigns.json"
		url = urljoin(self.base_url, location)
		headers = {"X-CSRFToken": self.csrf_token}
		json = {
			"banners": [{"content": {"image_240x400": {"id": image_id}}, "urls": {"primary": {"id": url_id}}}],
			"name": name,
			"objective": objective, "package_id": package_id}
		response = self.session.post(url=url, headers=headers, json=json)
		return response

	def delete_campaign(self, campaign_id):
		location = f"api/v2/campaigns/{campaign_id}.json"
		url = urljoin(self.base_url, location)
		headers = {"X-CSRFToken": self.csrf_token}
		response = self.session.delete(url=url, headers=headers)
		return response
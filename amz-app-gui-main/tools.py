import streamlit as st
import json, os

def change_page(page):
	def cp():
		st.session_state.page = page
	return cp


class Storage:
	def __init__(self, file_path):
		self.file_path = file_path
	
	def set(self, key, value):
		data = self._load_data()
		data[key] = value
		self._save_data(data)
	
	def get(self, key, default=None):
		data = self._load_data()
		return data.get(key, default)
	
	def clear(self):
		self._save_data({})
	
	def _load_data(self):
		if not os.path.exists(self.file_path):
			self._save_data({})
		with open(self.file_path, 'r') as file:
			data = json.load(file)
		return data
	
	def _save_data(self, data):
		with open(self.file_path, 'w') as file:
			json.dump(data, file)
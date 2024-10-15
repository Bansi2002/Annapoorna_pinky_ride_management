# Copyright (c) 2024, rider and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class RideBooking(Document):
	
	def validate(self):
		amount = 0 
		
		for ride_amount in self.services:
			if ride_amount.amount:
				amount += ride_amount.amount

		self.total_amount = (self.price_per_km * self.estimated_km) + amount
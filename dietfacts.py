# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Dietfacts_product_template(models.Model):

    _name = "product.template"
    _inherit = "product.template"

    calories = fields.Integer("Calories")
    servingsize = fields.Float("Serving Size")
    lastupdate  = fields.Date("Last Update")
    dietitem    = fields.Boolean("Diet Item")
    nutrient_ids = fields.One2many('product.template.nutrient', 'product_id', 'Nutrient')

class Dietfacts_res_users_meal(models.Model):

    _name = "res.users.meal"

    name = fields.Char('Meal Name')
    meal_time = fields.Datetime("Meal Time")
    user_id = fields.Many2one('res.users', 'Meal User')
    notes = fields.Text("Meal Notes")
    item_ids = fields.One2many('res.users.mealitems', 'meal_id')

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calcCalories(self):
        currCalories = 0
        for mealitem in self.item_ids:
            currCalories += mealitem.calories * mealitem.servings
        
        self.totalCalories = currCalories

    totalCalories = fields.Integer(string='Total Calories', store=True, compute='_calcCalories')

class DietFacts_res_user_mealitems(models.Model):
    _name = "res.users.mealitems"

    meal_id = fields.Many2one('res.users.meal')
    item_id = fields.Many2one("product.template", "Meal Items")
    servings = fields.Float("Serving")
    notes = fields.Text("Meal Item Notes")
    calories = fields.Integer(related="item_id.calories", string="Calories per Serving", store=True, readonly=True)

class DietFacts_product_nutrient(models.Model):
    _name = "product.nutrient"

    name = fields.Char("Nutrient Name")
    uom_id = fields.Many2one("product.uom", "Unit of Measure")
    description = fields.Text("Description")

class DietFacts_product_template_nutrient(models.Model):
	_name = "product.template.nutrient"

	nutrient_id = fields.Many2one("product.nutrient", string="Nutrient")
	product_id = fields.Many2one("product.template", string="Diet Item")
	value = fields.Float("Value")
	dailypercentage = fields.Float("Daily Percentage")
	unitofmeasure = fields.Char(related="nutrient_id.uom_id.name", string="Unit Of Measure" , readonly=True)

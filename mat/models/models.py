#-*- coding: utf-8 -*-

from odoo import models, fields, api
class mat(models.Model):
    _name = 'mat.course'
    _description = 'mat courses '

    name = fields.Char(string= "name ",required=True)
    description = fields.Text(' course discription')

    about = fields.Char(string="About ")
    addinfo = fields.Char(string="additional information")

    resposnsable_id= fields.Many2one('res.users', ondelete ='set null' ,string="Responsable" , index= True)
    session_id = fields.One2many('mat.sessions','course_id', string='sessions')



    # <!-- define new class   relationls between models -->


class sessions(models.Model):
    _name = 'mat.sessions'
    _description = 'mat sessions'

    name = fields.Char(string="TItle", required=True ,help= "write session name")
    start_date = fields.Datetime(string="start date", default= fields.Datetime.now())
    durations = fields.Float(string="numder of hourse", digits=(6,2))
    number_of_days = fields.Integer(string="number of days")
    seats = fields.Integer("Number of seats")

    instructor = fields.Char(string="instructor ")
    email = fields.Char(string="email")
    phone= fields.Char(string="phone")

    instructor_id = fields.Many2one('res.partner', string="instructor")
    course_id = fields.Many2one('mat.course' , ondelete='cascade', string='course' ,required=True)

    # attendent_id= fields.Many2many('res.partner', string="Attandantes")


# second class for course registerations

class registration(models.Model):
    _name = 'mat.registration'
    _description = 'student registration for specific course '

    name = fields.Char(string="student name", required=True ,help= "write session name")
    course_name= fields.Char(string="couresename", required= True)
    ident= fields.Integer(string=" identification id ")
    faculty= fields.Char(string="Fculty")
    major= fields.Char(string="major")
    start_date_reg = fields.Datetime(string="start date", default= fields.Datetime.now())


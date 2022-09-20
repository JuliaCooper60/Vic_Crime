# from .app import db


# class offence_division_summary(db.Model):
#     __tablename__ = 'offence_division_summary'

#     Year = db.Column(db.Integer)
#     Local_Government_Area = db.Column(db.Integer)
#     A_Crimes_against_the_person = db.Column(db.Integer)
#     B_Property_and_deception_offences = db.Column(db.Integer)
#     C_Drug_offences = db.Column(db.Integer)
#     D_Public_order_and_security_offences = db.Column(db.Integer)
#     E_Justice_procedures_offences = db.Column(db.Integer)
#     F_Other_offences = db.Column(db.Integer)

#     def __repr__(self):
#         return '<offence_division_summary %r>' % (self.name)

# class offence_2022(db.Model):
#     __tablename__ = 'offence_2022'

#     Year = db.Column(db.Integer)
#     Offence_Division = db.Column(db.String (64))
#     Offence_Subdivision = db.Column(db.String (64))
#     Offence_Subgroup = db.Column(db.String (64))
#     Incidents_Recorded = db.Column(db.Integer)
#     PSA_Rate_per_100000_population = db.Column(db.Float)
#     LGA_Rate_per_100000_population = db.Column(db.Float)
#     Local_Government_Area = db.Column(db.String (64))
#     Police_Service_Area = db.Column(db.String (64))
#     Police_Region = db.Column(db.String (64))
        
#     def __repr__(self):
#         return '<offence_2022 %r>' % (self.name)

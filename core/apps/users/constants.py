from django.db import models


class Gender(models.TextChoices):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class BloodType(models.TextChoices):
    A_RHD_POSITIVE = "A+"
    A_RHD_NEGATIVE = "A-"

    B_RHD_POSITIVE = "B+"
    B_RHD_NEGATIVE = "B-"

    O_RHD_POSITIVE = "O+"
    O_RHD_NEGATIVE = "O-"

    AB_RHD_POSITIVE = "AB+"
    AB_RHD_NEGATIVE = "AB-"


class UserType(models.TextChoices):
    ADMIN = "ADMIN"
    PATIENT = "PATIENT"
    SPECIALIST = "SPECIALIST"


class MedicalType(models.TextChoices):
    ALLERGY_AND_IMMUNOLOGY = 'ALLERGY_AND_IMMUNOLOGY'
    ANESTHESIOLOGY = 'ANESTHESIOLOGY'
    DERMATOLOGY = 'DERMATOLOGY'
    DIAGNOSTIC_RADIOLOGY = 'DIAGNOSTIC_RADIOLOGY'
    EMERGENCY_MEDICINE = 'EMERGENCY_MEDICINE'
    FAMILY_MEDICINE = 'FAMILY_MEDICINE'
    INTERNAL_MEDICINE = 'INTERNAL_MEDICINE'
    MEDICAL_GENETICS = 'MEDICAL_GENETICS'
    NEUROLOGY = 'NEUROLOGY'
    NUCLEAR_MEDICINE = 'NUCLEAR_MEDICINE'
    OBSTETRICS_AND_GYNECOLOGY = 'OBSTETRICS_AND_GYNECOLOGY'
    OPHTHALMOLOGY = 'OPHTHALMOLOGY'
    PATHOLOGY = 'PATHOLOGY'
    PEDIATRICS = 'PEDIATRICS'
    PHYSICAL_MEDICINE_AND_REHABILITATION = 'PHYSICAL_MEDICINE_AND_REHABILITATION'
    PREVENTIVE_MEDICINE = 'PREVENTIVE_MEDICINE'
    PSYCHIATRY = 'PSYCHIATRY'
    RADIATION_ONCOLOGY = 'RADIATION_ONCOLOGY'
    SURGERY = 'SURGERY'
    UROLOGY = 'UROLOGY'
    OTHER = 'OTHER'


class InternalCustomAdminActions(models.TextChoices):
    ADMIN_CREATE_NEW_USER = "ADMIN_CREATE_NEW_USER"
    ADMIN_CHANGE_USER_PASSWORD = "ADMIN_CHANGE_USER_PASSWORD"
    ADMIN_CHANGE_USER_INFO = "ADMIN_CHANGE_USER_INFO"
    REGISTERED_USER = "REGISTERED_USER"


class SpecialistType(models.TextChoices):
    BABY_CARE = "BABY_CARE"
    ELDERLY_CARE = "ELDERLY_CARE"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"
    PHYSICIAN = "PHYSICIAN"


class CollegesDegrees(models.TextChoices):
    PROFESSIONAL_CERTIFICATE = "PROFESSIONAL_CERTIFICATE"
    UNDERGRADUATE_DEGREE = "UNDERGRADUATE_DEGREE"
    TRANSFER_DEGREE = "TRANSFER_DEGREE"
    ASSOCIATE_DEGREE = "ASSOCIATE_DEGREE"
    BACHELOR_DEGREE = "BACHELOR_DEGREE"
    MASTER_DEGREE = "MASTER_DEGREE"
    DOCTORAL_DEGREE = "DOCTORAL_DEGREE"
    PROFESSIONAL_DEGREE = "PROFESSIONAL_DEGREE"
    SPECIALIST_DEGREE = "SPECIALIST_DEGREE"

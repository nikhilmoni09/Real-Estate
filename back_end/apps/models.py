from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


class Property(models.Model):
  property_name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  location = models.CharField(max_length=255)
  features = models.CharField(max_length=255)

  def __str__(self):
      return self.id


class Tenant(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  document_proofs = models.CharField(max_length=255)

  def __str__(self):
    return self.id


class Units(models.Model):
  rent_cost = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  tenant_id = models.ForeignKey("Tenant", on_delete=models.CASCADE)
  property_id = models.ForeignKey("Property", on_delete=models.CASCADE)
  agree_end_date = models.DateField(null=True)
  rent_date = models.DateField(null=True)
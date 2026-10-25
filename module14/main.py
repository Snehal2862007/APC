from patient.details import details as patient
from doctor.details import details as doctor
from billing.bill import bill
from records.history import history
print(patient(),doctor(),"bill:",bill(500,200),history())

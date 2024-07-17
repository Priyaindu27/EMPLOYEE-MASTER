from django.contrib import admin
from django.contrib import admin
from .models import BatchMaster
from .models import SemMaster
from .models import CourseMaster
from .models import PaperMaster
from .models import ExamMaster
from .models import StudentMaster
from .models import Transaction

# Register your models here.
admin.site.register(BatchMaster)
admin.site.register(SemMaster)
admin.site.register(CourseMaster)
admin.site.register(PaperMaster)
admin.site.register(ExamMaster)
admin.site.register(StudentMaster)
admin.site.register(Transaction)



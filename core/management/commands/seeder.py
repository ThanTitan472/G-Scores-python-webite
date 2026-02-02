from g_scores.models import Result
from django.core.management.base import BaseCommand
import csv, os
from django.conf import settings
from decimal import Decimal, InvalidOperation
# python manage.py seeder
def to_decimal(value):
    try:
        value = value.strip()
        return Decimal(value) if value != '' else None
    except (InvalidOperation, AttributeError):
        return None
class Command(BaseCommand):
    help = "Seed score data from CSV"
    def handle(self, *args, **options):
        csv_path = "mysite/data/diem_thi_thpt_2024.csv"
        if not os.path.exists(csv_path):
            csv_path = os.path.join(settings.BASE_DIR, "data", "diem_thi_thpt_2024.csv")
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Result.objects.create(
                    sbd=row["sbd"].strip(),
                    toan=to_decimal(row["toan"]),
                    ngu_van=to_decimal(row["ngu_van"]),
                    ngoai_ngu=to_decimal(row["ngoai_ngu"]),
                    vat_li=to_decimal(row["vat_li"]),
                    hoa_hoc=to_decimal(row["hoa_hoc"]),
                    sinh_hoc=to_decimal(row["sinh_hoc"]),
                    lich_su=to_decimal(row["lich_su"]),
                    dia_li=to_decimal(row["dia_li"]),
                    gdcd=to_decimal(row["gdcd"]),
                    ma_ngoai_ngu=row['ma_ngoai_ngu'].strip()
                )
        self.stdout.write(
            self.style.SUCCESS("Seed data successfully")
        )
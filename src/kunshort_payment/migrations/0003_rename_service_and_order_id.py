from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kunshort_payment', '0002_rename_order_id_to_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymenttransaction',
            old_name='service',
            new_name='reference_type',
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='reference_id',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]

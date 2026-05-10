from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kunshort_payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymenttransaction',
            old_name='order_id',
            new_name='service',
        ),
    ]

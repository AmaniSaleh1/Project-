
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jewelry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('designer', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('edition', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
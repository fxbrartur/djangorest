#!/bin/bash

echo ""

echo "Creating admin user and adminpass password"
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'adminpass')"

echo ""

echo "User and password were created successfully!"

echo ""
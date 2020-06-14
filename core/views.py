from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.facade import get_dashboard_data_summary


def index(request):
    return render(request, 'core/index.html')


@login_required
def dashboard(request):
    resumo = get_dashboard_data_summary()
    return render(request, 'dashboard.html', {'resumo': resumo})

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Handicapskydning import models

# Create your views here.


class Index(TemplateView):
    template_name = "index.html"


class Clubs(ListView):
    template_name = 'clubs.html'
    model = models.Club
    ordering = ['name', 'city']


class Gallery(ListView):
    template_name = "gallery.html"
    model = models.CPictures

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = models.Collections.objects.order_by('-year', 'name')
        return context


class Kalender(ListView):
    model = models.Activity
    template_name = "kalender.html"
    ordering = ['date']


class Lanes(ListView):
    template_name = 'lanes.html'
    model = models.Lane


class Links(ListView):
    template_name = 'links.html'
    model = models.Link
    ordering = ['name']


class News(ListView):
    model = models.News
    template_name = "news.html"
    ordering = ['date']


class Other(TemplateView):
    template_name = 'other.html'


class Results(ListView):
    template_name = "results.html"
    model = models.Results
    ordering = ['competition']


class Rules(ListView):
    template_name = 'rules.html'
    model = models.Documents
    ordering = ['name']


class Staff(ListView):
    template_name = "staff.html"
    model = models.Department
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_member'] = models.StaffMember.objects.order_by('name')
        return context


class StaffDetail(DetailView):
    template_name = 'staff-detail.html'
    model = models.StaffMember

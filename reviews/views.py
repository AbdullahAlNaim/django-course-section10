from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from .forms import ReviewForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

# Create your views here.

class ReviewView(CreateView):
    # this is used when using CreateView
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'

    # don't need this if using CreateView
    # form_class = ReviewForm

    # when not using FormView or CreateView but TemplateView
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()
    #
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })
    #
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/thank-you')
    #
    #     return render(request, 'reviews/review.html', {
    #         'form': form
    #     })


class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review # ListView -default template reference var name object_list
    context_object_name = 'reviews' # rename the template reference to this name

    # this is to adjust the data returned
    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gte=1)
        return data

    # this is when not using ListView but using TemplateView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context

    # this is when not using a TemplateView
    # def get(self, request):
    #     reviews = Review.objects.all()
    #     return render(request, 'reviews/review_list.html', {
    #         'reviews': reviews
    #     })

class SingleReviewView(DetailView):
    template_name = 'reviews/single_review.html'
    # make sure to change url /<int:id> to /<int:pk>
    model = Review # DetailView default template reference var name is object
    context_object_name = 'review' # rename the template reference to this name

    # this is when not using DetailView but just TemplateView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['id']
    #     single_review = Review.objects.get(pk=review_id)
    #     context['review'] = single_review
    #     return context

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works!'
        return context


# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#
#     else:
#         form = ReviewForm()
#
#     return render(request, 'reviews/review.html', {
#         'form': form
#     })
#

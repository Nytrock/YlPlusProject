from django.views.generic import TemplateView

from group.models import Meetup


class GroupListView(TemplateView):
    template_name = "group/group_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meetups"] = Meetup.meetups.meetup_list()
        return context


class GroupDetailView(TemplateView):
    template_name = 'group/group_detail.html'


class GroupCreateView(TemplateView):
    template_name = 'group/group_create.html'

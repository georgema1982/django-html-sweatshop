from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django_tables2.views import SingleTableMixin
from example.tables import DemoTable, DemoTable2
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'

class DiggPaginationRawView(TemplateView):
    
    template_name = 'digg_pagination_raw.html'
    
    def get_context_data(self, **kwargs):
        context = super(DiggPaginationRawView, self).get_context_data(**kwargs)
        object_list = range(100)
        paginator = Paginator(object_list, 5)
        page = self.request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = paginator.page(paginator.num_pages)
        context['page_obj'] = page_obj
        return context

class DiggPaginationTables2View(SingleTableMixin, TemplateView):
    template_name = 'digg_pagination_tables2.html'
    table_class = DemoTable
    table_data = [{'id': id} for id in xrange(100)]
    table_pagination = {'per_page': 5}

class Tables2View(DiggPaginationTables2View):
    template_name = 'tables2.html'
    table_class = DemoTable2

class MessageCentreView(TemplateView):
    
    template_name = 'message_centre.html'
    
    def get_context_data(self, **kwargs):
        request = self.request
        messages.info(request, 'This is an info')
        messages.success(request, 'This is a success')
        messages.warning(request, 'This is a warning')
        messages.error(request, 'This is an error')
        return super(MessageCentreView, self).get_context_data(**kwargs)

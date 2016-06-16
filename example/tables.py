from django_tables2.tables import Table
from django_tables2.columns.base import Column

class DemoTable(Table):
    id = Column()
    
    class Meta:
        attrs = {'class': 'paleblue'}

class DemoTable2(DemoTable):
    
    class Meta:
        attrs = {'class': 'table'}

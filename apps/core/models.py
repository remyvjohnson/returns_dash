from django.db import models
from django.db.models import Avg, Sum
import pygal
from pygal import Config
import heapq
from collections import OrderedDict, Counter

class core_return_reasons_sku(models.Model):
    ProductName = models.CharField(max_length=127)
    VariantName = models.CharField(max_length=127)
    SKU = models.CharField(max_length=127)
    ProductType = models.CharField(max_length=127)
    ProductCategory = models.CharField(max_length=127)
    ReasonID = models.IntegerField()
    Reason = models.CharField(max_length=127)
    ParentReason = models.CharField(max_length=127)
    Count = models.IntegerField()
    SalesUnits = models.IntegerField()


#--------------------------------------------------------------------------------------------#


class DashboardPanel(models.Model):
    dashboard_title = models.CharField(max_length=127, default=None, blank=True, null=True)
    dashboard_description = models.CharField(max_length=127, default=None, blank=True, null=True)
    dashboard_link = models.CharField(max_length=127, default=None, blank=True, null=True)
    panel_type = models.CharField(max_length=127, default=None, blank=True, null=True, choices=[
    ("barchart", "Bar Chart"),
    ("piechart", "Pie Chart"),
    ("table", "Table"),
    ])

    def __str__(self):
        return self.dashboard_title

    def cat_rr(self):
        category_names = [
            'Tops',
            'Bottoms',
            'Dresses',
            'Outerwear',
        ]

        return_percentages_by_category = {}
        for name in category_names:
            #Pulls and filters data; then calcs count and sales u sum
            return_sum = core_return_reasons_sku.objects.filter(
            ProductCategory=name).aggregate(Sum('Count'))
            return_sum_int = round(return_sum['Count__sum']) 

            sales_unit_sum = core_return_reasons_sku.objects.filter(
            ProductCategory=name).aggregate(Sum('SalesUnits'))
            sales_unit_sum_int = round(sales_unit_sum['SalesUnits__sum']) 

            # Converts to int, % and rounds 1 decimal place
            return_percentage = round((return_sum_int/sales_unit_sum_int)*100,1)  
            
            #adds to dict
            return_percentages_by_category[name] = return_percentage
            # print (name, return_percentage)
        
        return return_percentages_by_category
    
    
    
    def return_reason_percentages(self):
        #Pulls all reasons and assigns to variable
        full_list = core_return_reasons_sku.objects.values('Reason')

        #Loops through full_list and create a list of return reasons (no dups)
        rr_list = []
        for reason in range(len(full_list)):
            if full_list[reason]['Reason'] not in rr_list:
                rr_list.append(full_list[reason]['Reason'])               
    
        #Loops through rr_list and create a dict of reasons and rr%
        return_reason_percentages = {}
        for reason in rr_list:
            #Pulls and filters data; then calcs count and sales u sum
            return_sum = core_return_reasons_sku.objects.filter(
            Reason=reason).aggregate(Sum('Count'))
            return_sum_int = round(return_sum['Count__sum'])

            sales_unit_sum = core_return_reasons_sku.objects.filter(
            Reason=reason).aggregate(Sum('SalesUnits'))
            sales_unit_sum_int = round(sales_unit_sum['SalesUnits__sum'])

            # Converts to int, % and rounds 1 decimal place
            return_percentage = round((return_sum_int/sales_unit_sum_int)*100,1) 

            #adds to dict
            return_reason_percentages[reason] = return_percentage
        
        return return_reason_percentages

    
    def chart_options(self):
        data = self.return_reason_percentages()
        config = Config()
       
        if self.panel_type == 'barchart':
        
            bar_chart = pygal.Bar(show_legend = False, x_label_rotation=50, show_x_labels=True)
            # TODO figure out x-labels and show y-axis as %
            bar_chart.title = 'Return Reason %'
            for reason, avg in data.items():
                bar_chart.add(reason, avg)
            chart_svg_as_datauri = bar_chart.render_data_uri()
            return chart_svg_as_datauri

        elif self.panel_type == 'piechart':
            pie_chart = pygal.Pie(show_legend = False)
            pie_chart.title = 'Return Reason %'
            for reason, avg in data.items():
                pie_chart.add(reason, avg)
            chart_svg_as_datauri = pie_chart.render_data_uri()
            return chart_svg_as_datauri

        else:
            pass
       


    def highest_returned_styles(self):
        #Pulls styles and assigns to variable
        full_style_list = core_return_reasons_sku.objects.values('ProductName')

        #Loops through full_style_list and create a list of styles (no dups)
        style_list = []
        for style in range(len(full_style_list)):
            if full_style_list[style]['ProductName'] not in style_list:
                style_list.append(full_style_list[style]['ProductName'])                 
        # print(style_list)
    
        style_list_rr_percentages = {}
        for style in style_list:
            #Pulls and filters data; then calcs count and sales u sum
            return_sum = core_return_reasons_sku.objects.filter(
            ProductName=style).aggregate(Sum('Count'))
            return_sum_int = round(return_sum['Count__sum'])

            sales_unit_sum = core_return_reasons_sku.objects.filter(
            ProductName=style).aggregate(Sum('SalesUnits'))
            sales_unit_sum_int = round(sales_unit_sum['SalesUnits__sum'])

            # Converts to int, % and rounds 1 decimal place
            return_percentage = round((return_sum_int/sales_unit_sum_int)*100,1) 

            #adds to dict
            style_list_rr_percentages[style] = return_percentage
            # print (style, return_percentage)

        #pulls top 10 styles and rr%   
        top_return_styles = dict(Counter(style_list_rr_percentages).most_common(10))
        # print(top_return_styles)

        return top_return_styles
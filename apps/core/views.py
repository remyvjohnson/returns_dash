from django.shortcuts import render
from .models import core_return_reasons_sku, DashboardPanel
from django.db.models import Avg, Sum
import pygal
from pygal import Config
import heapq
from collections import OrderedDict, Counter


def home(request):
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


    context = {
        'category_data': return_percentages_by_category,
    }
    
    return render(request, 'pages/home.html', context)


#--------------------------------------------------------------------------------------------#


def return_reason_percentages():
    #Pulls all reasons and assigns to variable
    full_list = core_return_reasons_sku.objects.values('Reason')
    # print('still working')

    #Loops through full_list and create a list of return reasons (no dups)
    rr_list = []
    for reason in range(len(full_list)):
        if full_list[reason]['Reason'] not in rr_list:
            rr_list.append(full_list[reason]['Reason'])               
    # print(rr_list)
 
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
        # print (reason, return_percentage)
    
    return return_reason_percentages


#--------------------------------------------------------------------------------------------#

def bar_chart(request):
    # panels = DashboardPanel.objects.filter(category: category)
    panels = DashboardPanel.objects.all()
    # chart = DashboardPanel.objects.get(top_return_styles)

    context = {
        "panels": panels,
        # "charts": charts,
    }

    return render(request, 'pages/return_reasons.html', context)


#--------------------------------------------------------------------------------------------#

def highest_returned_styles(request):
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

    context = {
        'top_return_styles': top_return_styles,
    }

    return render(request, 'pages/top_return_styles.html', context)








#----------------------CODE PREGATORY---------------------------#
def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)


# def return_reason_bar_chart(request):
#     data = return_reason_percentages()
#     config = Config()
#     # TODO figure out x-labels and show y-axis as %
#     bar_chart = pygal.Bar(show_legend = False, x_label_rotation=50, show_x_labels=True)
#     bar_chart.title = 'Return Reason %'
#     for reason, avg in data.items():
#         bar_chart.add(reason, avg)

#     chart_svg_as_datauri = bar_chart.render_data_uri()

#     context = {
#         "rendered_chart": chart_svg_as_datauri,
#     }

#     return render(request, 'pages/return_reasons.html', context)


# def avg_return_counts_by_category():
#     category_names = [
#         'Tops',
#         'Bottoms',
#         'Dresses',
#         'Outerwear',
#     ]

#     avg_return_counts_by_category = {}
#     for name in category_names:
#         #Pulls and filters data; then gets the average count
#         avg_queryset = core_return_reasons_sku.objects.filter(
#         ProductCategory=name).aggregate(Avg('Count'))

#         #Converts to int and rounds to 2 decimal places
#         avg_return_int = round(avg_queryset['Count__avg'],2)    
        
#         #adds to dict
#         avg_return_counts_by_category[name] = avg_return_int
#         print (name, avg_return_int)
    
#     return avg_return_counts_by_category

# def pie_chart(request):
#     pie_chart = pygal.Pie()
#     data = return_reason_percentages(request)
#     for reason, avg in data.items():
#         pie_chart.title = 'Return Reasons'
#         pie_chart.add(reason, avg)

#     chart_svg_as_datauri = pie_chart.render_data_uri()


#     context = {
#         "rendered_chart": chart_svg_as_datauri,
#     }
#     print('---so far so good---')

#     return render(request, 'pages/return_reasons.html', context)




# def home(request):
    
#     return_reasons = core_return_reasons_sku.objects.all()
#     print('working')
#     context = {
#         'return_reasons': return_reasons,
#     }
#     return render(request, 'pages/home.html', context)



# return_reasons = core_return_reasons_sku.objects.all()
    # grouped_by_product_category = {}
    # for reason in return_reasons:
    #     category_name = reason["ProductCategory"]
    #     category_value = grouped_by_product_category[category_name]
    #     if category_value:
    #         category_value.append(reason)
    #     else:
    #         grouped_by_product_category[category_name] = [reason]

    # for key, value in grouped_by_product_category:
    #     print("key: ", key)
    #     print("value: ", value)
    
    # context = {
    #     'Product_Cat': grouped_by_product_category,
    # }




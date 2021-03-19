from django.shortcuts import render
from .models import core_return_reasons_sku, DashboardPanel
from django.db.models import Avg, Sum
import pygal
from pygal import Config
import heapq
from collections import OrderedDict, Counter


def home(request):
    dashboard_panels = DashboardPanel.objects.all()

    context = {
        "dashboard_panels": dashboard_panels,
    }
    
    return render(request, 'pages/home.html', context)


#--------------------------------------------------------------------------------------------#

def cat_rr(request):
    category_rates = DashboardPanel.objects.all()

    context = {
        "category_rates": category_rates,
    }

    return render(request, 'pages/rr_by_cat.html', context)


#--------------------------------------------------------------------------------------------#

def return_reasons(request):
    charts = DashboardPanel.objects.all()

    context = {
        "charts": charts,
    }

    return render(request, 'pages/return_reasons.html', context)


#--------------------------------------------------------------------------------------------#

def highest_returned_styles(request):
    top_return_styles = DashboardPanel.objects.all()

    context = {
        "top_return_styles": top_return_styles,
    }

    return render(request, 'pages/top_return_styles.html', context)








#----------------------CODE PURGATORY---------------------------#
# def about(request):
#     context = {
#     }

#     return render(request, 'pages/about.html', context)


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




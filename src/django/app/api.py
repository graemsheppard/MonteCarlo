from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import Http404
import datetime as dt
from shared.Monte import Monte


def simulate(request):
    """
    Generates the Monte object from the user input parameters in the request and reponds with an html string.
    """

    if request.method == 'GET':
        print(request.GET)

        ticker = str(request.GET.get("ticker", ''))
        sim_amount = int(request.GET.get("sim_amount", ''))
        time_steps = int(request.GET.get("time_steps", ''))
        start = dt.datetime.strptime((request.GET.get("start", '')), '%Y-%m-%d')
        end = dt.datetime.strptime((request.GET.get("end", '')), '%Y-%m-%d')
        
        monte_object = Monte(ticker=ticker, sim_amount=sim_amount, time_steps=time_steps, start=start, end=end)
        monte_object.create_DataFrame()
        monte_object.simulate()
        html_str1 = monte_object.plot_history()
        html_str2 = monte_object.plot_pdf()
        html_str3 = monte_object.plot_single()
        html_str4 = monte_object.plot_multi()

        html_str = monte_object.get_json(html_str1, html_str2, html_str3, html_str4)

        return HttpResponse(html_str)
    return HttpResponseBadRequest()

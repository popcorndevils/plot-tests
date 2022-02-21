import plotly.graph_objects as go
import ipywidgets as w
import pandas as pd
import random
import time
import threading

from IPython.display import clear_output, display

class Plotter:
    def __init__(self):
        self._RUN_THREAD = True
        self._output = w.Output()
        self._plot_display = w.Output()
        self._btn_show = w.Button(description = "Show")
        self._btn_show.on_click(self.handle_click)
        self._l_status = w.Label("HELLO")
        self._plot1 = None
        self._plot2 = None
        
    @property
    def RUN_THREAD(self):
        return self._RUN_THREAD
    
    @RUN_THREAD.setter
    def RUN_THREAD(self, value):
        if not value:
            self.display_plot()
        self._RUN_THREAD = value

    def run(self):
        with self._output:
            clear_output()
            display(self.widgets)
        return self._output

    @property
    def widgets(self):        
        _widgets = w.VBox([
            w.Label("TEST 1"),
            self._l_status,
            self._btn_show,
            self._plot_display,
        ])
        return _widgets
    
    def display_plot(self):

        g = go.FigureWidget()

        g.add_trace(self._plot1)
        g.add_trace(self._plot2)
        
        # g.update_layout(hovermode = "x unified")
        g.update_layout(hovermode = "x")

        with self._plot_display:
            clear_output()
            display(g)
        
    
    def update_status(self):
        _dots = [".", "..", "..."]
        i = 0
        while self.RUN_THREAD:
            self._l_status.value = f"RUNNING{_dots[i%3]}"
            i += 1
            time.sleep(.1)
        self._l_status.value = f"DONE"
            
    
    def update_plots(self):
        # https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.FigureWidget
        data = pd.DataFrame([{"day": f"day {x}", "hits": random.randint(0, 100)} for x in range(1, 100)])
        data2 = pd.DataFrame([{"day": f"day {x}", "hits": random.randint(0, 10)} for x in range(1, 100)])

        self._plot1 = go.Scatter(
            name = "full",
            x = data["day"],
            y = data["hits"],
            line = {"color": "blue", "width": 2},
            hovertemplate = "Price: $%{y:.2f}" + "<br>Week: %{x}"
        )
        
        time.sleep(1)

        self._plot2 = go.Scatter(
            name = "partial",
            x = data2["day"],
            y = data2["hits"],
            line = {"color": "red", "width": 2},
            hovertemplate = "Price: $%{y}" + "<br>Week: %{x}"
        )
        
        time.sleep(1)
        
        self.RUN_THREAD = False
        
        self.display_plot()
        

    def handle_click(self, _):
        self.RUN_THREAD = True
        thread1 = threading.Thread(target = self.update_status)
        thread2 = threading.Thread(target = self.update_plots)
        thread1.start()
        thread2.start()

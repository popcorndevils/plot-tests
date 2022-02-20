import plotly.graph_objects as go
import ipywidgets as w
import pandas as pd
import random

from IPython.display import clear_output, display

class Plotter:
    def __init__(self):
        self._output = w.Output()
        self._plot_display = w.Output()
        self._btn_show = w.Button(description = "Show")
        self._btn_show.on_click(self.handle_click)

    def run(self):
        with self._output:
            clear_output()
            display(self.widgets)
        return self._output

    @property
    def widgets(self):
        _widgets = w.VBox([
            w.Label("TEST 1"),
            self._btn_show,
            self._plot_display,
        ])
        return _widgets

    def handle_click(self, _):
        # https://plotly.com/python-api-reference/generated/plotly.graph_objects.html#plotly.graph_objects.FigureWidget
        data = pd.DataFrame([{"day": f"day {x}", "hits": random.randint(0, 100)} for x in range(1, 100)])
        data2 = pd.DataFrame([{"day": f"day {x}", "hits": random.randint(0, 10)} for x in range(1, 100)])

        g = go.FigureWidget()

        t1 = go.Scatter(
            name = "full",
            x = data["day"],
            y = data["hits"],
            line = {"color": "blue", "width": 2},
            hovertemplate = "Price: $%{y:.2f}" + "<br>Week: %{x}"
        )

        t2 = go.Scatter(
            name = "partial",
            x = data2["day"],
            y = data2["hits"],
            line = {"color": "red", "width": 2},
            hovertemplate = "Price: $%{y}" + "<br>Week: %{x}"
        )

        g.add_trace(t1)
        g.add_trace(t2)

        # g.update_layout(hovermode = "x unified")
        g.update_layout(hovermode = "x")

        with self._plot_display:
            clear_output()
            display(g)

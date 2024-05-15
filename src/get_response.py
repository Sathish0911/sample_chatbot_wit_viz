import re
import string
import random

def generate_visualization_html(response, code):

    visualization_code ='<div>' +\
                        '<img src="./static/images/icons8-chatbot-48.png" alt="Robot Logo" class="robot-logo">' +\
                        '&nbsp&nbsp&nbsp&nbsp' + response + '<br>' + code +\
                        '</div>'
    return visualization_code


def return_response(question):
            
    characters = string.ascii_letters + string.digits
    canvas_id = ''.join(random.choice(characters) for _ in range(24))

    greeting_patterns = re.compile(r"^(hi|hello|hey|greetings)(\s|$)", re.IGNORECASE)
    goodbye_patterns = re.compile(r"^(bye|goodbye|see you)(\s|$)", re.IGNORECASE)
    barchart_pattern = re.compile(r"^(bar|bar chart|bar graph)(\s|$)", re.IGNORECASE)
    piechart_pattern = re.compile(r"^(pie|pie chart| pie graph)(\s|$)", re.IGNORECASE)
    linechart_pattern = re.compile(r"^(line|line chart|line graph)(\s|$)", re.IGNORECASE)

    bar_chart = f"""
<div style="padding:20px;max-width: 850px;height: 350px;">
    <!-- Bar Chart -->
    <canvas id="{canvas_id}"></canvas>
    <script>
        var ctx = document.getElementById('{canvas_id}').getContext('2d');
        var myChart = new Chart(ctx, {{
            type: 'bar',
            data: {{
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [{{
                    label: 'Sales',
                    data: [1200, 1700, 1500, 2000, 1800],
                    backgroundColor: [
                        '#089297',
                        '#8B1F86',
                        '#AD2015',
                        '#F38D03',
                        '#E7ADD5'
                    ],
                    borderColor: [
                        '#089297',
                        '#8B1F86',
                        '#AD2015',
                        '#F38D03',
                        '#E7ADD5'
                    ],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    yAxes: [{{
                        ticks: {{
                            beginAtZero: true
                        }}
                    }}]
                }}
            }}
        }});
    </script>
</div>
"""
    pie_chart = f"""
<div style="padding:20px;max-width: 850px;height: 350px;">
    <!-- Pie Chart -->
    <canvas id="{canvas_id}"></canvas>
    <script>
        var ctx = document.getElementById('{canvas_id}').getContext('2d');
        var myChart = new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
                datasets: [{{
                    label: '# of Votes',
                    data: [12, 19, 3, 5, 2],
                    backgroundColor: [
                        '#370417',
                        '#CA6702',
                        '#F38D03',
                        '#FAD91D',
                        '#005C71'
                    ],
                    borderColor: [
                        '#370417',
                        '#CA6702',
                        '#F38D03',
                        '#FAD91D',
                        '#005C71'
                    ],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    yAxes: [{{
                        ticks: {{
                            beginAtZero: true
                        }}
                    }}]
                }}
            }}
        }});
    </script>
</div>
"""
    line_chart = f"""
<div style="padding:20px;max-width: 850px;height: 350px;">
    <!-- Line Chart -->
    <canvas id="{canvas_id}"></canvas>
    <script>
        var ctx = document.getElementById('{canvas_id}').getContext('2d');
        var myChart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: ['January', 'February', 'March', 'April', 'May'],
                datasets: [{{
                    label: 'Revenue',
                    data: [1000, 1200, 1300, 1100, 1500],
                    backgroundColor: [
                        '#AD2015'
                    ],
                    borderColor: [
                        '#AD2015'
                    ],
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    yAxes: [{{
                        ticks: {{
                            beginAtZero: true
                        }}
                    }}]
                }}
            }}
        }});
    </script>
</div>
"""

    # Check if user input matches any greeting patterns
    if greeting_patterns.match(question):
        return "Hello! How can I assist you?"

    # Check if user input matches any goodbye patterns
    elif goodbye_patterns.match(question):
        return "Goodbye! Have a great day!"
    
    elif barchart_pattern.match(question):
        return bar_chart
    
    elif piechart_pattern.match(question):
        return pie_chart
    
    elif  linechart_pattern.match(question):
        return line_chart
    
    else:
        return "Input does not match any pattern. Try typing bar graph, pie chart or line graph in user question"
    
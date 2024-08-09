try:
   import os
   import requests
   from rich.console import Console
   from rich.table import Table
except ImportError as e:
    print("Modules could not be imported. Have You Installed Them?")
console = Console()


api_key = "6d75ed911ffe4661b6a100104240907"
api_url = "http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_weather_data(city):
    try:
        
        response = requests.get(api_url.format(key=api_key, city=city))
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching data: {e}[/bold red]")
        return None

def display_weather(data, city):
    if data:
        table = Table(title=f"Weather in {city.title()}")
        table.add_column("", style="green")
        table.add_column("", style="green")
        table.add_row("Temperature", f"{data['current']['temp_c']}°C")
        table.add_row("Condition", data['current']['condition']['text'])
        table.add_row("Wind Speed", f"{data['current']['wind_kph']} km/h")
        table.add_row("Humidity", f"{data['current']['humidity']}%")
        
        clear_console()
        console.print(table)
    else:
        clear_console()
        console.print(f"[bold red]Could not retrieve weather data for {city}[/bold red]")

def app_menu():
    console.print("[bold green]Welcome to Weathex![/bold green]")
    while True:
        city_input = input("---Please enter the city name for which you want the weather displayed---\n").strip()
        
        if city_input.lower() == "exit":
            break
        
        weather_data = get_weather_data(city_input)
        
        if weather_data:
            display_weather(weather_data, city_input)
        else:
            console.print(f"[bold red] {city_input.title()} is not a valid city or data could not be fetched[/bold red]")

try:
    app_menu()
    console.print("[bold green]Thank you for using Weathex![/bold green]")
except Exception as e:
    console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

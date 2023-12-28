import calendar
import tkinter as tk

def create_calendar():
    def show_calendar():
        try:
            year = int(year_entry.get())
            if 1 <= year <= 9999:
                # Clear existing calendar if any
                for widget in calendar_frame.winfo_children():
                    widget.destroy()

                month_names = [
                    "January", "February", "March", "April",
                    "May", "June", "July", "August",
                    "September", "October", "November", "December"
                ]

                week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

                max_rows = 6  # Maximum number of rows to display for each month
                max_months = 12  # Total number of months to display

                padding_x = 5
                padding_y = 2

                for idx, month_name in enumerate(month_names[:max_months], start=1):
                    month_calendar = calendar.monthcalendar(year, idx)

                    row = (idx - 1) // 5  # Determine row placement
                    col = (idx - 1) % 5  # Determine column placement

                    month_frame = tk.Frame(calendar_frame, bg='white', bd=2, relief=tk.SOLID, highlightbackground="black")
                    month_frame.grid(row=row, column=col, padx=padding_x, pady=padding_y)  # Adding padding

                    month_label = tk.Label(month_frame, text=month_name, bg='white', fg='green', font=('Arial', 12, 'bold'))
                    month_label.pack()

                    inner_calendar_frame = tk.Frame(month_frame, bg='white')
                    inner_calendar_frame.pack(padx=padding_x, pady=padding_y)  # Adding padding

                    # Display week day names in column heading
                    for day_idx, day_name in enumerate(week_days):
                        day_label = tk.Label(inner_calendar_frame, text=day_name, width=3, height=1, bg='white', fg='blue')
                        day_label.grid(row=0, column=day_idx + 1)

                    # Display month calendar
                    for i in range(max_rows):
                        week = month_calendar[i] if i < len(month_calendar) else [0, 0, 0, 0, 0, 0, 0]
                        for day in week:
                            if day == 0:
                                day_label = tk.Label(inner_calendar_frame, text='', width=3, height=1, bg='white', fg='black')
                                day_label.grid(row=i + 1, column=week.index(day) + 1)
                            else:
                                day_label = tk.Label(inner_calendar_frame, text=str(day), width=3, height=1, bg='white', fg='black')
                                if calendar.weekday(year, idx, day) == 4:  # Check if it's a Friday
                                    day_label.config(fg='red')
                                day_label.grid(row=i + 1, column=week.index(day) + 1)
            else:
                raise ValueError("Invalid year")
        except ValueError as e:
            error_label.config(text="Please enter a valid year", fg="red")

    root = tk.Tk()
    root.title("Calendar")
    root.configure(bg='white')  # Setting background to white

    top_frame = tk.Frame(root, bg='white')
    top_frame.pack(pady=10)

    year_label = tk.Label(top_frame, text="Enter Year: ", bg='white', fg='black')
    year_label.pack(side=tk.LEFT)

    year_entry = tk.Entry(top_frame)
    year_entry.pack(side=tk.LEFT)

    show_button = tk.Button(top_frame, text="Show Calendar", command=show_calendar)
    show_button.pack(side=tk.LEFT)

    error_label = tk.Label(root, text="", bg='white')
    error_label.pack()

    calendar_frame = tk.Frame(root, bg='white')
    calendar_frame.pack()

    root.mainloop()

create_calendar()

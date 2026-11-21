

fees = {
    "Everest": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000},
    "Annapurna": {"Nepali": 100, "SAARC": 1000, "Foreign": 3000},
    "Langtang": {"Nepali": 100, "SAARC": 1500, "Foreign": 3000}
}

visitors = [
    ("Aarav", "Nepali", 22, "Everest"),
    ("Emma", "Foreign", 34, "Annapurna"),
    ("Rahul", "SAARC", 8, "Langtang"),
    ("John", "Foreign", 65, "Everest"),
    ("Mina", "Nepali", 30, "Annapurna"),
    ("Li", "Foreign", 28, "Everest")
]

revenue = {"Everest": 0, "Annapurna": 0, "Langtang": 0}
visitor_count = {"Everest": 0, "Annapurna": 0, "Langtang": 0}

categories = set()
total_revenue = 0

for name, category, age, area in visitors:

    fee = fees[area][category]

    if age < 10:
        fee = 0
    elif age >= 60:
        fee = fee // 2

    print(f"{name:<6} {area:<10} Rs {fee:>7}")

    revenue[area] += fee
    visitor_count[area] += 1
    categories.add(category)
    total_revenue += fee

busiest_area = max(visitor_count, key=visitor_count.get)

print("Revenue by area:", revenue)
print("Busiest area:", busiest_area,
      f"({visitor_count[busiest_area]} visitors)")
print("Visitor categories:", sorted(categories))
print("Total revenue: Rs", total_revenue)

#Q2. Restaurant orders and daily collection [5 marks]

menu = {
    1: ("Momo", 180),
    2: ("Chowmein", 150),
    3: ("Thakali Set", 450),
    4: ("Lassi", 120)
}

orders = [
    "1:2,4:2",
    "3:1,1:1,9:3",
    "2:3,1:2,4:1"
]

items_sold = {}
invalid_codes = []
total_collection = 0

for i, order in enumerate(orders, start=1):

    subtotal = 0

    pairs = order.split(",")

    for pair in pairs:

        code, quantity = pair.split(":")

        code = int(code)
        quantity = int(quantity)

        if code not in menu:
            invalid_codes.append(code)
            continue

        name, price = menu[code]

        subtotal += price * quantity

        if name not in items_sold:
            items_sold[name] = 0

        items_sold[name] += quantity

    service_charge = subtotal * 0.10
    vat = (subtotal + service_charge) * 0.13

    final_bill = subtotal + service_charge + vat

    total_collection += final_bill

    print(f"Table {i}: subtotal Rs {subtotal}, "
          f"bill with service + VAT Rs {final_bill:.2f}")

best_seller = max(items_sold, key=items_sold.get)

print("Items sold:", items_sold)
print("Best seller:", best_seller, "| Invalid codes:", invalid_codes)
print(f"Day's collection: Rs {total_collection:.2f}")


#Q3. Cricket ball-by-ball scorecard [5 marks]

balls = "1 4 . W 6 wd 2 1 . 4 nb 1 . . W 6 1 lb2"

ball_list = balls.split()

score = 0
wickets = 0
legal_balls = 0
extras = 0
fours = 0
sixes = 0
dot_balls = 0

for ball in ball_list:

    if ball == "wd":
        score += 1
        extras += 1
        continue

    elif ball == "nb":
        score += 1
        extras += 1
        continue

    elif ball == "W":
        wickets += 1
        legal_balls += 1

    elif ball == ".":
        dot_balls += 1
        legal_balls += 1

    elif ball == "lb2":
        score += 2
        extras += 2
        legal_balls += 1

    else:
        runs = int(ball)
        score += runs
        legal_balls += 1

        if runs == 4:
            fours += 1
        elif runs == 6:
            sixes += 1

overs = legal_balls // 6
remaining_balls = legal_balls % 6

run_rate = score / (legal_balls / 6)

boundary_runs = (fours * 4) + (sixes * 6)

boundary_percentage = (boundary_runs / score) * 100

print(f"Score: {score}/{wickets} in {overs}.{remaining_balls} overs")

print(f"Extras {extras}, Fours {fours}, Sixes {sixes}, "
      f"Dot balls {dot_balls}")

print(f"Run rate {run_rate:.2f}, Boundary runs {boundary_runs} "
      f"({boundary_percentage:.1f}% of total)")


#Q4. Data analyst job shortlisting [5 marks]


required = {"python", "sql", "excel", "statistics"}

applicants = [
    {"name": "Ram", "age": 24, "cgpa": 3.4,
     "skills": {"python", "excel", "html"}},

    {"name": "Sita", "age": 37, "cgpa": 3.8,
     "skills": {"python", "sql", "excel", "statistics"}},

    {"name": "Gita", "age": 26, "cgpa": 3.6,
     "skills": {"python", "sql", "statistics", "tableau"}},

    {"name": "Hari", "age": 29, "cgpa": 2.7,
     "skills": {"sql", "excel", "statistics", "python"}}
]

interview_order = []
extra_skills = set()

for applicant in applicants:

    name = applicant["name"]
    age = applicant["age"]
    cgpa = applicant["cgpa"]
    skills = applicant["skills"]

    matched = skills.intersection(required)
    missing = required.difference(skills)

    extra_skills.update(skills.difference(required))

    if age < 21 or age > 35:
        print(f"{name}: rejected (age {age})")
        continue

    match_percentage = (len(matched) / len(required)) * 100

    if match_percentage >= 75 and cgpa >= 2.5:

        print(f"{name}: {match_percentage:.0f}% match, "
              f"shortlisted, missing {sorted(missing)}")

        interview_order.append((name, match_percentage, cgpa))

    else:

        print(f"{name}: {match_percentage:.0f}% match, "
              f"not shortlisted, missing {sorted(missing)}")

# Sort by match percentage, then CGPA (highest first)
interview_order.sort(key=lambda x: (-x[1], -x[2]))

print("Interview order:", [x[0] for x in interview_order])
print("Extra skills seen (not required):", sorted(extra_skills))



#Q5. Rainfall stations and flood watch [5 marks]

rain = {
    "Kathmandu": [0, 12.5, 70.2, 118.0, 40.1, 0, 1.2],
    "Pokhara": [35.0, 88.4, 20.3, 95.0, 5.0, 0, 0],
    "Biratnagar": [0, 0, 2.0, 10.5, 66.0, 210.5, 130.0]
}

totals = {}
heavy_stations = set()

for station, readings in rain.items():

    total = sum(readings)
    rainy_days = 0
    max_rain = max(readings)
    peak_day = readings.index(max_rain) + 1

    streak = 0
    flood_watch = False

    for value in readings:

        if value > 0:
            rainy_days += 1

        if value >= 64.5:
            heavy_stations.add(station)
            streak += 1

            if streak >= 2:
                flood_watch = True

        else:
            streak = 0

    if flood_watch:
        status = "FLOOD WATCH"
    else:
        status = "normal"

    totals[station] = total

    print(f"{station:<12} total {total:6.1f} mm, "
          f"rainy days {rainy_days}, "
          f"peak {max_rain:.1f} mm on day {peak_day}, {status}")

wettest_station = max(totals, key=totals.get)

print("Wettest station:", wettest_station)
print("Stations with heavy rain:", sorted(heavy_stations))


#Q6. Mobile game match history [5 marks]

matches = [
    ("W", 10, 1, 5, "Layla"),
    ("W", 3, 2, 4, "Tigreal"),
    ("L", 2, 6, 3, "Layla"),
    ("W", 8, 0, 6, "Gusion"),
    ("W", 5, 2, 9, "Layla"),
    ("W", 1, 3, 12, "Tigreal"),
    ("L", 4, 5, 2, "Gusion"),
    ("W", 7, 2, 8, "Layla")
]

wins = 0
current_streak = 0
longest_streak = 0

hero_kda = {}

for result, kills, deaths, assists, hero in matches:

    if result == "W":
        wins += 1
        current_streak += 1

        if current_streak > longest_streak:
            longest_streak = current_streak

    else:
        current_streak = 0

    if deaths == 0:
        kda = kills + assists
    else:
        kda = (kills + assists) / deaths

    if hero not in hero_kda:
        hero_kda[hero] = []

    hero_kda[hero].append(kda)

win_rate = (wins / len(matches)) * 100

print(f"Win rate: {win_rate:.1f}%  "
      f"Longest win streak: {longest_streak}")

for hero, kdas in hero_kda.items():

    games = len(kdas)
    average_kda = sum(kdas) / games

    print(f"{hero:<9} games {games}, avg KDA {average_kda:.2f}")

most_played = max(hero_kda, key=lambda hero: len(hero_kda[hero]))

print("Most played hero:", most_played)


#Q7. Glacier lake outburst early warning [5 marks]

lakes = {
    "Tsho Rolpa": (20.0, 24.0,
                   [17.2, 17.5, 18.3, 19.0, 20.1, 22.0, 24.4, 25.0]),

    "Imja": (15.0, 18.0,
             [12.0, 12.1, 12.3, 12.2, 12.6, 13.0, 13.1, 13.3]),

    "Thulagi": (30.0, 33.0,
                [28.0, 28.9, 29.5, 30.2, 30.4, 30.1, 29.8, 29.6])
}

status_groups = {
    "Normal": [],
    "Watch": [],
    "Danger": []
}

for lake, data in lakes.items():

    warning, danger, readings = data

    rises = []

    for i in range(1, len(readings)):
        rise = readings[i] - readings[i - 1]
        rises.append(round(rise, 2))

    max_level = max(readings)
    biggest_rise = max(rises)

    status = "Normal"
    warning_hour = None

    for hour, level in enumerate(readings):

        if level >= danger:
            status = "Danger"
            warning_hour = hour
            break

        elif level >= warning and status == "Normal":
            status = "Watch"
            warning_hour = hour

    # Check for 3 consecutive rises greater than 0.5 m
    rapid_rise = False
    consecutive_rises = 0

    for rise in rises:

        if rise > 0.5:
            consecutive_rises += 1

            if consecutive_rises >= 3:
                rapid_rise = True
        else:
            consecutive_rises = 0

    if status == "Normal":
        status_groups["Normal"].append(lake)

    elif status == "Watch":
        status_groups["Watch"].append(lake)

    else:
        status_groups["Danger"].append(lake)

    if status == "Normal":
        status_text = "Normal"

    else:
        status_text = f"{status} (from hour {warning_hour})"

    if rapid_rise:
        status_text += " + RAPID RISE"

    print(f"{lake:<12} max {max_level:.1f} m, "
          f"biggest rise {biggest_rise:.1f} m, "
          f"status {status_text}")

print(status_groups)

if status_groups["Danger"]:
    print("EVACUATE downstream of:",
          ", ".join(status_groups["Danger"]))


#Q8. Forest fire risk by district and province [5 marks]
districts = [
    ("Chitwan", "Bagmati", 36, 18, 25, 40),
    ("Kaski", "Gandaki", 27, 55, 10, 5),
    ("Dang", "Lumbini", 33, 30, 35, 20),
    ("Bardiya", "Lumbini", 38, 15, 32, 35),
    ("Ilam", "Koshi", 24, 70, 8, 3),
    ("Makwanpur", "Bagmati", 31, 40, 18, 12)
]

risk_groups = {
    "Low": [],
    "Moderate": [],
    "High": [],
    "Extreme": []
}

provinces_to_alert = set()

for name, province, temp, humidity, wind, days in districts:

    score = 0

    # Temperature scoring
    if temp > 35:
        score += 3
    elif temp > 30:
        score += 2
    elif temp > 25:
        score += 1

    # Humidity scoring
    if humidity < 20:
        score += 3
    elif humidity < 35:
        score += 2
    elif humidity < 50:
        score += 1

    # Wind scoring
    if wind > 30:
        score += 2
    elif wind > 15:
        score += 1

    # Days since rain scoring
    if days > 30:
        score += 3
    elif days > 14:
        score += 2
    elif days > 7:
        score += 1

    # Determine risk level
    if score >= 9:
        risk = "Extreme"
    elif score >= 7:
        risk = "High"
    elif score >= 4:
        risk = "Moderate"
    else:
        risk = "Low"

    risk_groups[risk].append((name, score))

    if risk == "High" or risk == "Extreme":
        provinces_to_alert.add(province)

for risk, districts_list in risk_groups.items():

    print(f"{risk:<9}: {districts_list}")

print("Provinces to alert:", sorted(provinces_to_alert))



#Q9. Smart Nepal electricity meters [5 marks]


meters = {
    "H-101": [1200, 1265, 1340, 1520, 1590],
    "H-102": [880, 910, 945, 975, 1010],
    "H-103": [2300, 2420, 2470, 2530, 2700]
}

slabs = [
    (20, 4),
    (30, 7),
    (50, 9),
    (float("inf"), 11)
]

total_revenue = 0
spikes = []

for house, readings in meters.items():

    monthly_units = []

    # Calculate monthly consumption
    for i in range(1, len(readings)):

        consumption = readings[i] - readings[i - 1]
        monthly_units.append(consumption)

    average = sum(monthly_units) / len(monthly_units)

    # Calculate latest month's bill
    remaining_units = monthly_units[-1]
    bill = 0

    for units, rate in slabs:

        if remaining_units <= 0:
            break

        billed_units = min(remaining_units, units)

        bill += billed_units * rate
        remaining_units -= billed_units

    total_revenue += bill

    print(f"{house}: monthly units {monthly_units}, "
          f"avg {average:.1f}, latest bill Rs {bill}")

    # Detect consumption spikes
    for i in range(1, len(monthly_units)):

        previous = monthly_units[i - 1]
        current = monthly_units[i]

        if current > previous * 1.5:

            spikes.append((house, i + 1, previous, current))

print("Spikes (>50% jump):")

for house, month, previous, current in spikes:

    print(f"  {house} month {month}: "
          f"{previous} -> {current} units")

print("Total latest-month revenue: Rs", total_revenue)


#Q10. Restaurant and cafe review analysis [5 marks]


reviews = [
    ("Momo Magic", 5,
     "Delicious momo and friendly staff, very clean place"),

    ("Momo Magic", 4,
     "Tasty food but slow service"),

    ("Thakali Kitchen", 2,
     "Food was cold and the place was dirty"),

    ("Thakali Kitchen", 3,
     "Good dal bhat but expensive and slow"),

    ("Lakeside Cafe", 5,
     "Amazing view, delicious coffee, friendly owner")
]

positive = {
    "delicious", "friendly", "clean",
    "tasty", "good", "amazing"
}

negative = {
    "slow", "cold", "dirty", "expensive", "rude"
}

ratings = {}
review_counts = {}
word_counts = {}

for place, stars, review in reviews:

    # Clean the review
    cleaned = review.lower().replace(",", "")

    words = cleaned.split()

    # Convert words into a set for matching
    word_set = set(words)

    pos_words = word_set.intersection(positive)
    neg_words = word_set.intersection(negative)

    # Count matching words
    pos_count = sum(words.count(word) for word in pos_words)
    neg_count = sum(words.count(word) for word in neg_words)

    if pos_count > neg_count:
        mood = "Positive"
    elif pos_count < neg_count:
        mood = "Negative"
    else:
        mood = "Mixed"

    print(f"{place:<16} {stars}* "
          f"pos={pos_count} neg={neg_count} -> {mood}")

    # Store ratings per place
    if place not in ratings:
        ratings[place] = 0
        review_counts[place] = 0

    ratings[place] += stars
    review_counts[place] += 1

    # Count positive and negative opinion words
    for word in words:

        if word in positive or word in negative:

            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1

print("Average rating:")

for place in ratings:

    average = ratings[place] / review_counts[place]

    print(f"  {place:<16} {average:.1f} "
          f"from {review_counts[place]} reviews")

# Sort by frequency (highest first), then alphabetically
top_words = sorted(
    word_counts.items(),
    key=lambda x: (-x[1], x[0])
)

print("Top opinion words:", top_words[:3])
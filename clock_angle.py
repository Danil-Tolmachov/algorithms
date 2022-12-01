# Набросать код, который будет рассчитывать угол между часовой и минутной
# стрелкой в заданное время. Данная задача покажет логическое мышление
# кандидата, и как быстро он сможет придумать решение.

def clock_angle(hours: int, seconds: int) -> float:
    degree_hours = 360/24 * hours
    degree_seconds = 360/60 * seconds

    if abs(degree_hours - degree_seconds) < 180:
        return abs(degree_hours - degree_seconds)
    else:
        return abs(degree_seconds - degree_hours)


assert clock_angle(12, 30) == 0
assert clock_angle(12, 15) == 90
assert clock_angle(12, 60) == 180

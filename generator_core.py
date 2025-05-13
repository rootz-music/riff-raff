
import random

def generate_bars(persona, theme, flex, chaos):
    bars = []
    for _ in range(4):
        subject = random.choice(["ice", "jacket", "python", "Versace", "jet ski", "lava lamp", "gummy bears", "hair dye"])
        verb = random.choice(["glow", "drip", "hiss", "teleport", "breathe", "bounce"])
        obj = random.choice(["in the club", "in my trunk", "from the ceiling", "on my wrist", "in the matrix"])
        swag = f"My {subject} {verb}s {obj}."
        if chaos > 7:
            swag += f" {random.choice(['Yuh!', 'Flexed too hard!', 'Chromed out DNA!'])}"
        bars.append(swag)
    return "\n".join(bars)

def generate_hook(persona, theme, flex, chaos):
    hook = []
    base = random.choice(["Came through drippin'", "High-waist flex", "Mood ring activated", "Pulled up neon"])
    response = random.choice(["Michelle Obama", "Skittles and drama", "tuned like Nirvana", "snakes in pajamas"])
    for _ in range(2):
        hook.append(f"{base}... {response}")
    return "\n".join(hook)

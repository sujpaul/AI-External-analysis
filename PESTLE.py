from manim import *
from manim import config
config.media_width = "1920"  # Optional: Set resolution
config.save_last_frame = True

class PESTLEDiagram(Scene):
    def construct(self):
        # Define categories and their items
        categories = {
            "Political": {
                "items": ["AI regulations", "Government funding", "Data sovereignty"],
                "type": "Management",
                "color": BLUE,
            },
            "Economic": {
                "items": ["Cost reduction", "Market trends", "Funding sources"],
                "type": "Operational",
                "color": GREEN,
            },
            "Social": {
                "items": ["Public trust", "Workforce training", "Ethics"],
                "type": "Management",
                "color": ORANGE,
            },
            "Technological": {
                "items": ["Algorithm innovation", "Cloud infrastructure", "Cybersecurity"],
                "type": "Operational",
                "color": PURPLE,
            },
            "Legal": {
                "items": ["Compliance laws", "IP rights", "Privacy policies"],
                "type": "Management",
                "color": RED,
            },
            "Environmental": {
                "items": ["Energy efficiency", "Carbon footprint", "Sustainability goals"],
                "type": "Operational",
                "color": YELLOW,
            },
        }

        # Positioning parameters
        start_x = -4
        start_y = 3
        box_width = 3.5
        box_height = 2
        x_spacing = 4.5
        y_spacing = 2.5

        # Store created boxes for linking
        boxes = []

        # Create boxes for each category
        for i, (category, details) in enumerate(categories.items()):
            # Calculate position
            x = start_x + (i % 2) * x_spacing
            y = start_y - (i // 2) * y_spacing

            # Create rectangle with title and items
            rect = RoundedRectangle(width=box_width, height=box_height, color=details["color"], corner_radius=0.2)
            rect.move_to([x, y, 0])

            # Title
            title = Text(category, font_size=18, weight=BOLD).move_to(rect.get_top() + DOWN * 0.3)

            # Items
            item_text = VGroup(
                *[Text(f"- {item}", font_size=14) for item in details["items"]]
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(rect.get_center())

            # Group everything together
            group = VGroup(rect, title, item_text)
            self.add(group)
            boxes.append((category, rect, details["type"], item_text))

        # Add linkage arrows for related categories
        self.wait(1)
        self.add(Text("Links between PESTLE factors", font_size=20).to_edge(UP))

        # Example connections
        self.play(
            *[
                Create(Arrow(start=boxes[0][1].get_edge_center(RIGHT), end=boxes[3][1].get_edge_center(LEFT), color=WHITE)),
                Create(Arrow(start=boxes[2][1].get_edge_center(RIGHT), end=boxes[4][1].get_edge_center(LEFT), color=WHITE)),
                Create(Arrow(start=boxes[1][1].get_edge_center(DOWN), end=boxes[5][1].get_edge_center(UP), color=WHITE)),
            ]
        )

        # Legend for Management and Operational
        legend_management = VGroup(
            RoundedRectangle(width=1, height=0.5, color=BLUE).next_to(boxes[-1][1], RIGHT, buff=1),
            Text("Management", font_size=14).next_to(boxes[-1][1], RIGHT, buff=1.5),
        )
        legend_operational = VGroup(
            RoundedRectangle(width=1, height=0.5, color=GREEN).next_to(legend_management[0], DOWN, buff=0.3),
            Text("Operational", font_size=14).next_to(legend_management[1], DOWN, buff=0.3),
        )

        self.play(FadeIn(legend_management), FadeIn(legend_operational))

        self.wait(3)

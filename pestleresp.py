from manim import *

class PESTLEResponsibleAI(Scene):
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

        # Add Responsible AI as a cross-cutting theme
        responsible_ai_items = [
            "Fairness in AI systems",
            "Transparency in decision-making",
            "Accountability frameworks",
            "Bias detection and mitigation",
        ]

        # Positioning parameters
        center_x = 0
        center_y = 0
        radius = 3.5  # Distance from the center for the categories

        # Store created boxes for linking
        boxes = []

        # Create Responsible AI box in the center
        responsible_ai_box = RoundedRectangle(
            width=4.5, height=2.5, color=GOLD, corner_radius=0.3
        ).move_to([center_x, center_y, 0])

        responsible_ai_title = Text("Responsible AI", font_size=20, weight=BOLD).move_to(
            responsible_ai_box.get_top() + DOWN * 0.3
        )

        responsible_ai_text = VGroup(
            *[Text(f"- {item}", font_size=14) for item in responsible_ai_items]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(responsible_ai_box.get_center())

        self.add(responsible_ai_box, responsible_ai_title, responsible_ai_text)

        # Create boxes for each category in a circular layout
        for i, (category, details) in enumerate(categories.items()):
            angle = i * (2 * PI / len(categories))  # Equally space categories in a circle
            x = center_x + radius * np.cos(angle)
            y = center_y + radius * np.sin(angle)

            # Create rectangle with title and items
            rect = RoundedRectangle(width=3.5, height=2, color=details["color"], corner_radius=0.2)
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

        # Connect Responsible AI to all PESTLE categories with arrows
        for _, rect, _, _ in boxes:
            arrow = Arrow(start=responsible_ai_box.get_edge_center(UP), end=rect.get_center(), color=WHITE)
            self.add(arrow)

        # Add legend for Management and Operational
        legend_management = VGroup(
            RoundedRectangle(width=1, height=0.5, color=BLUE).to_edge(DR, buff=1.5),
            Text("Management", font_size=14).next_to(RIGHT, buff=0.3),
        )
        legend_operational = VGroup(
            RoundedRectangle(width=1, height=0.5, color=GREEN).next_to(legend_management[0], DOWN, buff=0.3),
            Text("Operational", font_size=14).next_to(legend_management[1], DOWN, buff=0.3),
        )

        self.add(legend_management, legend_operational)

        # Ensure the final frame is saved
        self.wait(1)

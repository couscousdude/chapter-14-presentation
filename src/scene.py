from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        intro = Tex(
            r"Consider the function $e^x$. \\We can represent it as a series expansion of polynomial terms as follows:",
        ).set(font_size=30)

        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x",
        )
        equation.set_color_by_tex("x", YELLOW)

        intro.next_to(equation, UP, buff=0.5)

        self.play(Write(intro))
        self.play(Write(equation))


class Intro(Scene):
    def construct(self):
        quote_template = TexTemplate().add_to_preamble(r"\usepackage{attrib}")
        quote = Tex(
            r"""\begin{quote} “Capitalism as it exists today is, in my
                opinion, the real source of evils. I am convinced there
                is only one way to eliminate these grave evils, namely
                through the establishment of a socialist economy,
                accompanied by an educational system which would be
                oriented toward social goals. In such an economy, the
                means of production are owned by society itself and are
                utilized in a planned fashion.” \end{quote}
                \attrib{Albert Einstein, Why Socialism?}
                """,
            tex_template=quote_template,
            font_size=30,
        )

        self.play(
            Write(
                quote,
            ),
            run_time=5,
        )


class MyBeautifulGraph(Scene):
    def construct(self):
        axes = Axes(axis_config={"include_tip": False})

        self.play(Write(axes))


def table_four_three():
    axes = Axes(
        x_length=4,
        y_length=4,
        x_range=[0, 5],
        y_range=[0, 5],
        axis_config={"include_tip": False, "include_ticks": False},
    )
    return axes


class Slide1(Scene):
    def construct(self):
        intro = Tex(
            r"""
            The Essence of Macroeconomics
            """,
            font_size=72,
        )
        # self.add(labels)
        self.play(Write(intro), run_time=5)
        self.play(Unwrite(intro))

        title = Tex(
            r"A Traveler's Guide to Interest Rates\\and Monetary Policy", font_size=50
        )

        self.play(Write(title), run_time=3)
        self.wait(1)
        self.play(Unwrite(title))

        author = Tex(r"By Youwen Wu, Charles Krueger, and Isaac Chen")
        self.play(Write(author), run_time=5)

        graph = table_four_three()

        graph.scale(0.4).next_to(author, DOWN, buff=0.7).shift(RIGHT * 1.75)

        labels = graph.get_axis_labels(
            Tex(r"Quantity of Reserves").scale(0.3),
            Tex(r"Federal Funds Rate (\%)").scale(0.3),
        )

        line1_1 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[3.75, 3.75],
            line_color=RED,
            add_vertex_dots=False,
        )

        line1_1_label = MathTex(
            r"S_{f^3}",
            font_size=12,
        ).next_to(line1_1, RIGHT * 0.2)
        line2_1 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[2.5, 2.5],
            line_color=RED,
            add_vertex_dots=False,
        )
        line2_1_label = MathTex(
            r"S_{f^1}",
            font_size=12,
        ).next_to(line2_1, RIGHT * 0.2)
        # label2 = line2.
        line3_1 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[1.25, 1.25],
            line_color=RED,
            add_vertex_dots=False,
        )
        line3_1_label = MathTex(
            r"S_{f^2}",
            font_size=12,
        ).next_to(line3_1, RIGHT * 0.2)

        diag_1_line = graph.plot_line_graph(
            x_values=[0.5, 4],
            y_values=[4.25, 0.75],
            line_color=GREEN,
            add_vertex_dots=False,
        )
        diag_line_1_label = MathTex(r"D_f", font_size=12).next_to(
            diag_1_line, DOWN * 0.15 + RIGHT * 0.3
        )

        # Create axes
        axes = (
            Axes(
                x_length=2,
                y_length=2,
                x_range=[100, 200],
                y_range=[0, 20],
                axis_config={"include_tip": False, "include_ticks": False},
            )
            .scale(0.8)
            .next_to(author, DOWN, buff=0.7)
            .shift(LEFT * 1.75)
        )

        labels_2 = axes.get_axis_labels(
            Tex(
                r"Amount of money demanded\\and supplied\\(billions of dollars)",
                font_size=24,
            ).scale(0.3),
            Tex(r"Real rate of interest (\%)", font_size=24).scale(0.3),
        )

        line1 = axes.plot_line_graph(
            x_values=[125, 125],
            y_values=[0, 18],
            line_color=RED,
            add_vertex_dots=False,
        )
        line2 = axes.plot_line_graph(
            x_values=[150, 150],
            y_values=[0, 18],
            line_color=RED,
            add_vertex_dots=False,
        )
        line3 = axes.plot_line_graph(
            x_values=[175, 175],
            y_values=[0, 18],
            line_color=RED,
            add_vertex_dots=False,
        )
        line1_label_top = MathTex(
            r"S_{m^1}",
            font_size=14,
        ).next_to(line1, UP * 0.2)
        line2_label_top = MathTex(
            r"S_{m^2}",
            font_size=14,
        ).next_to(line2, UP * 0.2)
        line3_label_top = MathTex(
            r"S_{m^3}",
            font_size=14,
        ).next_to(line3, UP * 0.2)

        diag_line = axes.plot_line_graph(
            x_values=[105, 195],
            y_values=[17, 2],
            line_color=GREEN,
            add_vertex_dots=False,
        )
        diag2_line_label = MathTex(r"D_m", font_size=14).next_to(
            diag_line, DOWN * 0.15 + RIGHT * 0.3
        )
        construction_line1 = axes.plot_line_graph(
            x_values=[100, 125],
            y_values=[13.5, 13.5],
            line_color=GRAY,
            add_vertex_dots=True,
        )
        construction_line2 = axes.plot_line_graph(
            x_values=[100, 150],
            y_values=[9.5, 9.5],
            line_color=GRAY,
            add_vertex_dots=True,
        )
        construction_line3 = axes.plot_line_graph(
            x_values=[100, 175],
            y_values=[5.25, 5.25],
            line_color=GRAY,
            add_vertex_dots=True,
        )
        construction_line1_label = MathTex(
            r"10",
            font_size=14,
        ).next_to(construction_line1, LEFT * 0.2)
        construction_line2_label = MathTex(
            r"8",
            font_size=14,
        ).next_to(construction_line2, LEFT * 0.2)
        construction_line3_label = MathTex(
            r"6",
            font_size=14,
        ).next_to(construction_line3, LEFT * 0.2)

        line1_label_bottom = MathTex(
            r"125",
            font_size=14,
        ).next_to(line1, DOWN * 0.2)
        line2_label_bottom = MathTex(
            r"150",
            font_size=14,
        ).next_to(line2, DOWN * 0.2)
        line3_label_bottom = MathTex(
            r"175",
            font_size=14,
        ).next_to(line3, DOWN * 0.2)

        self.wait(1)

        self.play(
            Create(graph),
            Create(labels),
            Create(line1_1),
            Write(line1_1_label),
            Write(line2_1_label),
            Write(line3_1_label),
            Create(line2_1),
            Create(line3_1),
            Create(diag_1_line),
            Write(diag_line_1_label),
            Create(axes),
            Create(diag_line),
            Create(line1),
            Create(line2),
            Create(line3),
            Write(line1_label_top),
            Write(line2_label_top),
            Write(line3_label_top),
            Create(construction_line1),
            Create(construction_line2),
            Create(construction_line3),
            Write(diag2_line_label),
            Write(construction_line1_label),
            Write(construction_line2_label),
            Write(construction_line3_label),
            Write(line1_label_bottom),
            Write(line2_label_bottom),
            Write(line3_label_bottom),
            Write(labels_2),
        )

        self.wait(3)

        self.play(
            Unwrite(graph),
            Unwrite(labels),
            Unwrite(line1_1),
            Unwrite(line1_1_label),
            Unwrite(line2_1_label),
            Unwrite(line3_1_label),
            Unwrite(line2_1),
            Unwrite(line3_1),
            Unwrite(diag_1_line),
            Unwrite(diag_line_1_label),
            Unwrite(axes),
            Unwrite(diag_line),
            Unwrite(line1),
            Unwrite(line2),
            Unwrite(line3),
            Unwrite(line1_label_top),
            Unwrite(line2_label_top),
            Unwrite(line3_label_top),
            Unwrite(construction_line1),
            Unwrite(construction_line2),
            Unwrite(construction_line3),
            Unwrite(diag2_line_label),
            Unwrite(construction_line1_label),
            Unwrite(construction_line2_label),
            Unwrite(construction_line3_label),
            Unwrite(line1_label_bottom),
            Unwrite(line2_label_bottom),
            Unwrite(line3_label_bottom),
            Unwrite(labels_2),
            run_time=0.5,
        )
        self.play(Unwrite(author))


class Slide2(Scene):
    def construct(self):
        title = Tex(r"An Overview of Interest Rates", font_size=60).shift(UP * 2.3)
        line1 = Tex(
            r"""\begin{enumerate}
                    \item Interest can be thought of as the price paid for using money
                    \item The demand for money comes from transactions demand and asset demand
                    \item The supply of money and demand for money determine the equilibrium interest rate
                    \item Bond prices and interest rates have an inverse relationship
                \end{enumerate}
                    """,
            font_size=30,
        )
        line2 = MathTex(
            r"""
            \text{Interest Rate}\ \propto \frac{1}{\text{Bond Price}} \Longleftrightarrow \text{Bond Price}\ \propto \frac{1}{\text{Interest Rate}}
            """,
            font_size=30,
        ).next_to(line1, DOWN * 1.5)

        self.play(Write(title), Write(line1))
        self.play(Write(line2))


class Slide3(Scene):
    def construct(self):
        title = Tex(r"The Demand for Money", font_size=60).shift(UP * 2.3)
        caption = Tex(
            r"""
                Why hold on to money?
            """,
            font_size=50,
        ).next_to(title, DOWN, buff=0.7)
        line1 = Tex(
            r"""
                \medskip
                \begin{enumerate}
                    \item Transactions demand: demand for money as a medium of exchange
                    \item Asset demand: the amount of money people want to hold as a store of value
                \end{enumerate}
                    """,
            font_size=30,
        ).next_to(caption, DOWN, buff=0.3)

        self.play(Write(title))
        self.play(Write(caption))
        self.play(Write(line1))


class Slide4(Scene):
    def construct(self):
        title = Tex(r"Transactions Demand", font_size=60).shift(UP * 2.3)

        definition = (
            Tex(
                r"\textbf{Definition}: The amount of money people want\\to hold as a {{ medium of exchange }}",
            )
            .set_color_by_tex("medium of exchange", "YELLOW")
            .next_to(title, DOWN, buff=0.7)
        )

        line1 = Tex(
            r"""
                \medskip
                \begin{enumerate}
                    \item People need money on hand to purchase goods and services
                    \item Directly correlated with nominal (pre-adjusted) GDP
                    \item Level of nominal GDP determines the amount of money demanded for transactions
                \end{enumerate}
                    """,
            font_size=30,
        ).next_to(definition, DOWN, buff=0.5)

        math = MathTex(
            r"""
                \uparrow~\text{Nominal GDP} \implies \uparrow~\text{Money demanded}
            """
        ).next_to(line1, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(definition))
        self.play(Write(line1))
        self.play(Write(math))
        self.play(Indicate(definition))
        self.play(Indicate)


class Slide5(Scene):
    def construct(self):
        title = Tex(r"Asset Demand", font_size=60).shift(UP * 2.3)

        definition = (
            Tex(
                r"\textbf{Definition}: The amount of money people want\\to hold as a {{ store of value }}",
            )
            .set_color_by_tex("store of value", "YELLOW")
            .next_to(title, DOWN, buff=0.7)
        )

        line1 = Tex(
            r"""
                \medskip
                \begin{enumerate}
                    \item People hold financial assets in many forms, including money, since it's the most liquid
                    \item Main disadvantage: money holds no interest
                    \item Interest rate inversely determines asset demand for money
                \end{enumerate}
                    """,
            font_size=30,
        ).next_to(definition, DOWN, buff=0.7)

        math = MathTex(
            r"""
                \uparrow~\text{Interest rates} \implies \downarrow~\text{Money demanded}
            """
        ).next_to(line1, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(definition))
        self.play(Write(line1))
        self.play(Write(math))
        self.play(Indicate(definition))
        self.play(Indicate(math))


class Slide6(Scene):
    def construct(self):
        figure = ImageMobject("/src/assets/figFourteenOne.png")

        self.play(Write(figure))

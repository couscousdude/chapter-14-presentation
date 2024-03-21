from manim import *


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

        title = Tex(r"Interest Rates and Monetary Policy", font_size=50)
        self.play(
            Transform(intro, title, replace_mobject_with_target_in_scene=True),
            run_time=3,
        )

        self.wait(1)
        self.play(Unwrite(title), run_time=3)

        author = Tex(r"By Youwen Wu, Charles Krueger, and Isaac Chen")
        self.play(
            Write(author),
            run_time=5,
        )

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

        title = Tex(r"Figure 14.1", font_size=60).shift(UP * 2.3)

        figure = (
            ImageMobject("./src/assets/figFourteenOne.png")
            .next_to(title, DOWN, buff=1)
            .scale(1.5)
        )

        self.play(Write(title))
        self.play(FadeIn(figure))


class Slide7(Scene):
    def construct(self):
        title = Tex(r"Figure 14.1", font_size=60).shift(UP * 2.3)

        figure = (
            ImageMobject("./src/assets/figFourteenOne.png")
            .next_to(title, DOWN, buff=1)
            .scale(1.5)
        )

        self.add(title)
        self.add(figure)

        self.play(figure.animate.scale(0.5).shift(UP * 2.3))
        self.play(title.animate.scale(0.3).next_to(figure, DOWN, buff=0.15))

        explanation = Tex(
            r"""
                            \begin{itemize}
                                \item Vertical line represents transactions demand's independence from the influence of interest rates
                                \item Downward sloping line represents asset demand's inverse relationship with interest rates
                                \item Total demand for money is the sum of transactions demand and asset demand
                                \item Money supply and total money demand graph represents money market and determines equilibrium interest rate
                            \end{itemize}
                        """,
            font_size=20,
        ).next_to(figure, DOWN, buff=0.7)

        eq = MathTex(r"D_m = D_t + D_a").next_to(explanation, DOWN, buff=0.3)

        self.play(Write(explanation))
        self.play(Write(eq))

        self.play(Indicate(title))
        self.play(Indicate(eq))


class Slide8(Scene):
    def construct(self):
        title = Tex(r"Figure 14.1", font_size=60).shift(UP * 2.3)

        figure = (
            ImageMobject("./src/assets/figFourteenOne.png")
            .next_to(title, DOWN, buff=1)
            .scale(1.5)
        )

        self.add(figure.scale(0.5).shift(UP * 2.3))
        self.add(title.scale(0.3).next_to(figure, DOWN, buff=0.15))

        explanation = Tex(
            r"""
                            \begin{itemize}
                                \item Vertical line represents transactions demand's independence from the influence of interest rates
                                \item Downward sloping line represents asset demand's inverse relationship with interest rates
                                \item Total demand for money is the sum of transactions demand and asset demand
                                \item Money supply and total money demand graph represents money market and determines equilibrium interest rate
                            \end{itemize}
                        """,
            font_size=20,
        ).next_to(figure, DOWN, buff=0.7)

        eq = MathTex(r"D_m = D_t + D_a").next_to(explanation, DOWN, buff=0.3)

        self.add(explanation)
        self.add(eq)

        self.play(Unwrite(eq))
        self.play(Unwrite(explanation))

        self.play(figure.animate.scale(2.5).shift(DOWN * 2.3))
        self.play(title.animate.scale(2).next_to(figure, UP, buff=0.4))

        header = Tex(r"What's up with that graph?", font_size=64).move_to(title)

        self.play(Transform(title, header, replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(Indicate(header))


class Slide9(Scene):
    def construct(self):
        title = Tex(r"Interest Rates", font_size=60).shift(UP * 2.3)

        line1 = (
            Tex(
                r"""
                \medskip
                \begin{enumerate}
                    \item \textbf{Equilibrium interest rate}: the supply of money equals the demand for money in the economy
                    \item Rise in money supply lowers equilibrium interest rate, vice versa ($S_m \propto \frac{1}{I_e}$)
                    \item Level of nominal GDP determines the amount of money demanded for transactions
                \end{enumerate}
                    """,
                font_size=30,
            )
        ).next_to(title, DOWN, buff=0.7)

        line2 = (
            Tex(
                r"""
            {{ Interest Rates }} and {{ Bond Prices }} are closely and inversely related.
            """,
                font_size=30,
            )
            .next_to(line1, DOWN, buff=0.7)
            .set_color_by_tex("Bond Prices", "RED")
            .set_color_by_tex("Interest Rates", "BLUE")
        )

        equation = MathTex(
            r"""\text{Interest Rate}~\uparrow \implies \text{Bond Price}~\downarrow"""
        ).next_to(line2, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(equation))

        self.play(Indicate(line2))


class Slide9Supplement2(Scene):
    def construct(self):
        title = Tex(r"Interest Rates", font_size=60).shift(UP * 2.3)
        text_line1 = (
            Tex(
                r"""
                The following graph shows three different equilibrium interest rates:
                \medskip
                    """,
                font_size=26,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.add(title)
        self.add(text_line1)

        # Create axes
        axes = (
            Axes(
                x_length=2,
                y_length=2,
                x_range=[100, 200],
                y_range=[0, 20],
                axis_config={"include_tip": False, "include_ticks": False},
            )
            .scale(1.6)
            .next_to(text_line1, DOWN, buff=0.7)
        )

        labels_2 = axes.get_axis_labels(
            Tex(
                r"Amount of money demanded\\and supplied\\(billions of dollars)",
                font_size=24,
            ).scale(0.8),
            Tex(r"Real rate of interest (\%)", font_size=24).scale(0.8),
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
            font_size=18,
        ).next_to(line1, UP * 0.2)
        line2_label_top = MathTex(
            r"S_{m^2}",
            font_size=18,
        ).next_to(line2, UP * 0.2)
        line3_label_top = MathTex(
            r"S_{m^3}",
            font_size=18,
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
            font_size=18,
        ).next_to(construction_line1, LEFT * 0.2)
        construction_line2_label = MathTex(
            r"8",
            font_size=18,
        ).next_to(construction_line2, LEFT * 0.2)
        construction_line3_label = MathTex(
            r"6",
            font_size=18,
        ).next_to(construction_line3, LEFT * 0.2)

        line1_label_bottom = MathTex(
            r"125",
            font_size=18,
        ).next_to(line1, DOWN * 0.2)
        line2_label_bottom = MathTex(
            r"150",
            font_size=18,
        ).next_to(line2, DOWN * 0.2)
        line3_label_bottom = MathTex(
            r"175",
            font_size=18,
        ).next_to(line3, DOWN * 0.2)

        self.add(
            axes,
            labels_2,
            line1,
            line2,
            line3,
            line1_label_top,
            line2_label_top,
            line3_label_top,
            diag_line,
            diag2_line_label,
            construction_line1,
            construction_line2,
            construction_line3,
            construction_line1_label,
            construction_line2_label,
            construction_line3_label,
            line1_label_bottom,
            line2_label_bottom,
            line3_label_bottom,
        )

        new_title = Tex(r"What's up with that graph?", font_size=60).shift(UP * 2.3)
        new_line1 = (
            Tex(
                r"""
                Explain the significance of the points on the graph and its slope.
                \medskip
                    """,
                font_size=26,
            )
        ).next_to(new_title, DOWN, buff=0.7)

        self.play(
            Transform(title, new_title, replace_mobject_with_target_in_scene=True),
            Transform(text_line1, new_line1),
        )

        self.wait(0.5)

        self.play(Indicate(title))


class Slide9Supplement(Scene):
    def construct(self):
        title = Tex(r"Interest Rates", font_size=60).shift(UP * 2.3)
        text_line1 = (
            Tex(
                r"""
                The following graph shows three different equilibrium interest rates:
                \medskip
                    """,
                font_size=26,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(text_line1))

        # Create axes
        axes = (
            Axes(
                x_length=2,
                y_length=2,
                x_range=[100, 200],
                y_range=[0, 20],
                axis_config={"include_tip": False, "include_ticks": False},
            )
            .scale(1.6)
            .next_to(text_line1, DOWN, buff=0.7)
        )

        labels_2 = axes.get_axis_labels(
            Tex(
                r"Amount of money demanded\\and supplied\\(billions of dollars)",
                font_size=24,
            ).scale(0.8),
            Tex(r"Real rate of interest (\%)", font_size=24).scale(0.8),
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
            font_size=18,
        ).next_to(line1, UP * 0.2)
        line2_label_top = MathTex(
            r"S_{m^2}",
            font_size=18,
        ).next_to(line2, UP * 0.2)
        line3_label_top = MathTex(
            r"S_{m^3}",
            font_size=18,
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
            font_size=18,
        ).next_to(construction_line1, LEFT * 0.2)
        construction_line2_label = MathTex(
            r"8",
            font_size=18,
        ).next_to(construction_line2, LEFT * 0.2)
        construction_line3_label = MathTex(
            r"6",
            font_size=18,
        ).next_to(construction_line3, LEFT * 0.2)

        line1_label_bottom = MathTex(
            r"125",
            font_size=18,
        ).next_to(line1, DOWN * 0.2)
        line2_label_bottom = MathTex(
            r"150",
            font_size=18,
        ).next_to(line2, DOWN * 0.2)
        line3_label_bottom = MathTex(
            r"175",
            font_size=18,
        ).next_to(line3, DOWN * 0.2)

        self.play(Create(axes))
        self.play(Write(labels_2))
        self.play(Create(line1))
        self.play(Create(line2))
        self.play(Create(line3))
        self.play(Write(line1_label_top))
        self.play(Write(line2_label_top))
        self.play(Write(line3_label_top))
        self.play(Create(diag_line))
        self.play(Write(diag2_line_label))
        self.play(Create(construction_line1))
        self.play(Create(construction_line2))
        self.play(Create(construction_line3))
        self.play(Write(construction_line1_label))
        self.play(Write(construction_line2_label))
        self.play(Write(construction_line3_label))
        self.play(Write(line1_label_bottom))
        self.play(Write(line2_label_bottom))
        self.play(Write(line3_label_bottom))


class Slide10(Scene):
    def construct(self):
        title = Tex(r"Tools of Monetary Policy", font_size=60).shift(UP * 2.3)

        line1 = (
            Tex(
                r"""The Fed has {{ 3 tools }} to control/alter\\commercial banking system reserves"""
            )
            .set_color_by_tex("3 tools", "YELLOW")
            .next_to(title, DOWN, buff=0.7)
        )

        line2 = (
            Tex(
                r"""
                \medskip
                \begin{enumerate}
                    \item Open market operations
                    \item Reserve ratio
                    \item Discount rate
                \end{enumerate}""",
                font_size=30,
            )
        ).next_to(line1, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2))


class Slide11(Scene):
    def construct(self):
        title = Tex(r"Open Market Operations", font_size=60).shift(UP * 2.3)

        line1 = Tex(
            r"""\textbf{Definition}: The buying of money and
                 government bonds (securities) from,\\ or selling of
                 to, commercial banks and the public""",
            font_size=30,
        ).next_to(title, DOWN, buff=0.7)

        line2 = (
            Tex(
                r"""
                \medskip When Fed buys from {{ banks}},{{ bank's }}
                reserves increase,\\increases lending capabilities from 
                {{ banks}}. 
                """,
                font_size=28,
            )
            .set_color_by_tex("bank", "RED")
            .next_to(line1, DOWN, buff=0.4)
        )

        line3 = (
            Tex(
                r"""
                \medskip When Fed buys from {{ public}}, similar
                result,\\lending capabilities of banks and money supply
                increase
                """,
                font_size=28,
            )
            .set_color_by_tex("public", "BLUE")
            .next_to(line2, DOWN, buff=0.4)
        )

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))


class Slide12(Scene):
    def construct(self):
        title = Tex(r"Reserve Ratio", font_size=60).shift(UP * 2.3)

        line1 = Tex(
            r"""\textbf{Definition}: The percentage of deposits a financial institution must hold in reserve as cash""",
            font_size=30,
        ).next_to(title, DOWN, buff=0.7)

        line2 = (
            Tex(
                r"""
                \medskip
                \begin{enumerate}
                    \item Raising reserve ratio: banks keep more, reducing overall money supply
                    \item Lowering reserve ratio: banks keep less, lending abilities increase, increases money supply
                \end{enumerate}""",
                font_size=30,
            )
        ).next_to(line1, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2))


class Slide13(Scene):
    def construct(self):
        title = Tex(
            r"Table 14.2: Effects of Changes in the Reserve Ratio", font_size=48
        ).shift(UP * 2.3)

        table_template = TexTemplate()
        table_template.add_to_preamble(r"\usepackage{multirow}")

        line1 = (
            Tex(
                r"""
                    \begin{tabular}{|c|c|c|c|c|c|c|}
                        \hline
                        \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}reserve\\ ratio, r\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}checkable\\ deposits\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}actual\\ reserves\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}required\\ reserves\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}excess \\ reserves,\\ (3) - (4)\end{tabular}} & \multicolumn{2}{c|}{money-creating potential of} \\ \cline{6-7} 
                        &  &  &  &  & \multicolumn{1}{c|}{\begin{tabular}[c]{@{}c@{}}single bank, = (5)\end{tabular}} & \begin{tabular}[c]{@{}c@{}}entire \\ banking system\end{tabular} \\ \hline
                        (1) 10 & \$20,000 & \$5000 & \$2000 & \$ 3000 & \$ 3000 & \$30,000 \\ \hline
                        (2) 20 & 20,000 & 5000 & 4000 & 1000 & 1000 & 5000 \\ \hline
                        (3) 25 & 20,000 & 5000 & 5000 & 0 & -- & 0 \\ \hline
                        (4) 30 & 20,000 & 5000 & 6000 & -1000 & -1000 & -3333 \\ \hline
                        \end{tabular}
                """,
                font_size=30,
                tex_template=table_template,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.play(Write(title), Write(line1), run_time=4)


class Slide14(Scene):
    def construct(self):
        title = Tex(
            r"Table 14.2: Effects of Changes in the Reserve Ratio", font_size=48
        ).shift(UP * 2.3)

        table_template = TexTemplate()
        table_template.add_to_preamble(r"\usepackage{multirow}")

        line1 = (
            Tex(
                r"""
                    \begin{tabular}{|c|c|c|c|c|c|c|}
                        \hline
                        \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}reserve\\ ratio, r\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}checkable\\ deposits\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}actual\\ reserves\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}required\\ reserves\end{tabular}} & \multirow{2}{*}{\begin{tabular}[c]{@{}c@{}}excess \\ reserves,\\ (3) - (4)\end{tabular}} & \multicolumn{2}{c|}{money-creating potential of} \\ \cline{6-7} 
                        &  &  &  &  & \multicolumn{1}{c|}{\begin{tabular}[c]{@{}c@{}}single bank, = (5)\end{tabular}} & \begin{tabular}[c]{@{}c@{}}entire \\ banking system\end{tabular} \\ \hline
                        (1) 10 & \$20,000 & \$5000 & \$2000 & \$ 3000 & \$ 3000 & \$30,000 \\ \hline
                        (2) 20 & 20,000 & 5000 & 4000 & 1000 & 1000 & 5000 \\ \hline
                        (3) 25 & 20,000 & 5000 & 5000 & 0 & -- & 0 \\ \hline
                        (4) 30 & 20,000 & 5000 & 6000 & -1000 & -1000 & -3333 \\ \hline
                        \end{tabular}
                """,
                font_size=30,
                tex_template=table_template,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.add(title, line1)

        new_title = Tex(r"What's up with this chart?", font_size=60).shift(UP * 2.3)

        self.play(Transform(title, new_title))

        self.play(Indicate(line1))


class Slide15(Scene):
    def construct(self):
        title = Tex(r"Discount Rate", font_size=60).shift(UP * 2.3)

        line1 = Tex(
            r"""\textbf{Definition}: Rate the Fed charges on loans they grant to commercial banks""",
            font_size=30,
        ).next_to(title, DOWN, buff=0.7)

        line2 = (
            Tex(
                r"""
                \medskip
                \begin{enumerate}
                    \item The Fed is a last-resort lender, so the Fed charges the discount rate on loans it grants to banks
                    \item Raising discount rate $\implies$ commercial banks more reluctant to take loans from the Fed, restricting money supply
                \end{enumerate}""",
                font_size=30,
            )
        ).next_to(line1, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2))


class Slide16(Scene):
    def construct(self):
        title = Tex(r"Federal Funds Rate", font_size=60).shift(UP * 2.3)

        line1 = (
            Tex(
                r"""
                    \begin{enumerate}
                        \item The Fed targets the Federal funds rate -- the rate banks charge each other for overnight loans of reserves
                        \item It adjusts the money supply via open-market operations to move the Federal funds rate to the desired target level
                        \item Changes in the Federal funds rate influence other market rates like the prime rate
                    \end{enumerate}""",
                font_size=30,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))


class Slide18(Scene):
    def construct(self):
        title = Tex(
            r"Figure 14.3: Targetting the Federal funds rate", font_size=48
        ).shift(UP * 2.3)

        self.add(title)
        # self.play(Write(line1))

        graph = table_four_three()

        graph.next_to(title, DOWN, buff=0.7)

        labels = graph.get_axis_labels(
            Tex(r"Quantity of Reserves").scale(0.7),
            Tex(r"Federal Funds Rate (\%)").scale(0.7),
        )

        line1 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[3.75, 3.75],
            line_color=RED,
            add_vertex_dots=False,
        )

        line1_label_right = MathTex(
            r"S_{f^3}",
            font_size=18,
        ).next_to(line1, RIGHT * 0.2)

        line1_label_left = MathTex(
            r"4.5",
            font_size=18,
        ).next_to(line1, LEFT * 0.4)

        line2 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[2.5, 2.5],
            line_color=RED,
            add_vertex_dots=False,
        )
        line2_label_right = MathTex(
            r"S_{f^1}",
            font_size=18,
        ).next_to(line2, RIGHT * 0.2)

        line2_label_left = MathTex(
            r"4",
            font_size=18,
        ).next_to(line2, LEFT * 0.4)
        # label2 = line2.
        line3 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[1.25, 1.25],
            line_color=RED,
            add_vertex_dots=False,
        )
        line3_label_right = MathTex(
            r"S_{f^2}",
            font_size=18,
        ).next_to(line3, RIGHT * 0.2)

        line3_label_left = MathTex(
            r"3.5",
            font_size=18,
        ).next_to(line3, LEFT * 0.4)

        diag_line = graph.plot_line_graph(
            x_values=[0.5, 4],
            y_values=[4.25, 0.75],
            line_color=GREEN,
            add_vertex_dots=False,
        )
        diag_line_label = MathTex(r"D_f", font_size=18).next_to(
            diag_line, DOWN * 0.15 + RIGHT * 0.3
        )

        construction_line1 = graph.plot_line_graph(
            x_values=[1, 1],
            y_values=[0, 3.75],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line2 = graph.plot_line_graph(
            x_values=[2.25, 2.25],
            y_values=[0, 2.5],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line3 = graph.plot_line_graph(
            x_values=[3.5, 3.5],
            y_values=[0, 1.25],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line1_label = MathTex(
            r"Q_{f^3}",
            font_size=18,
        ).next_to(construction_line1, DOWN * 0.2)

        construction_line2_label = MathTex(
            r"Q_{f^1}",
            font_size=18,
        ).next_to(construction_line2, DOWN * 0.2)

        construction_line3_label = MathTex(
            r"Q_{f^2}",
            font_size=18,
        ).next_to(construction_line3, DOWN * 0.2)

        self.add(
            graph,
            labels,
            line1,
            line1_label_right,
            line2,
            line2_label_right,
            line3,
            line3_label_right,
            diag_line,
            diag_line_label,
            line1_label_left,
            line2_label_left,
            line3_label_left,
        )

        self.add(
            construction_line1,
            construction_line2,
            construction_line3,
            construction_line1_label,
            construction_line2_label,
            construction_line3_label,
        )

        new_title = Tex(r"What's up with this graph?", font_size=48).shift(UP * 2.3)

        self.play(Transform(title, new_title))

        self.play(
            Indicate(line1),
            Indicate(line2),
            Indicate(line3),
            Indicate(diag_line),
            Indicate(construction_line1),
            Indicate(construction_line2),
            Indicate(construction_line3),
            Indicate(graph),
        )

        self.play(
            Indicate(line1_label_right),
            Indicate(line2_label_right),
            Indicate(line3_label_right),
        )

        self.play(
            Indicate(line1_label_left),
            Indicate(line2_label_left),
            Indicate(line3_label_left),
        )

        self.play(
            Indicate(construction_line1_label),
            Indicate(construction_line2_label),
            Indicate(construction_line3_label),
        )

        self.wait(1)


class Slide17(Scene):
    def construct(self):
        title = Tex(
            r"Figure 14.3: Targetting the Federal funds rate", font_size=48
        ).shift(UP * 2.3)

        self.play(Write(title))
        # self.play(Write(line1))

        graph = table_four_three()

        graph.next_to(title, DOWN, buff=0.7)

        labels = graph.get_axis_labels(
            Tex(r"Quantity of Reserves").scale(0.7),
            Tex(r"Federal Funds Rate (\%)").scale(0.7),
        )

        line1 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[3.75, 3.75],
            line_color=RED,
            add_vertex_dots=False,
        )

        line1_label_right = MathTex(
            r"S_{f^3}",
            font_size=18,
        ).next_to(line1, RIGHT * 0.2)

        line1_label_left = MathTex(
            r"4.5",
            font_size=18,
        ).next_to(line1, LEFT * 0.4)

        line2 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[2.5, 2.5],
            line_color=RED,
            add_vertex_dots=False,
        )
        line2_label_right = MathTex(
            r"S_{f^1}",
            font_size=18,
        ).next_to(line2, RIGHT * 0.2)

        line2_label_left = MathTex(
            r"4",
            font_size=18,
        ).next_to(line2, LEFT * 0.4)
        # label2 = line2.
        line3 = graph.plot_line_graph(
            x_values=[0, 4],
            y_values=[1.25, 1.25],
            line_color=RED,
            add_vertex_dots=False,
        )
        line3_label_right = MathTex(
            r"S_{f^2}",
            font_size=18,
        ).next_to(line3, RIGHT * 0.2)

        line3_label_left = MathTex(
            r"3.5",
            font_size=18,
        ).next_to(line3, LEFT * 0.4)

        diag_line = graph.plot_line_graph(
            x_values=[0.5, 4],
            y_values=[4.25, 0.75],
            line_color=GREEN,
            add_vertex_dots=False,
        )
        diag_line_label = MathTex(r"D_f", font_size=18).next_to(
            diag_line, DOWN * 0.15 + RIGHT * 0.3
        )

        construction_line1 = graph.plot_line_graph(
            x_values=[1, 1],
            y_values=[0, 3.75],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line2 = graph.plot_line_graph(
            x_values=[2.25, 2.25],
            y_values=[0, 2.5],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line3 = graph.plot_line_graph(
            x_values=[3.5, 3.5],
            y_values=[0, 1.25],
            line_color=RED,
            add_vertex_dots=True,
            stroke_width=1,
        )

        construction_line1_label = MathTex(
            r"Q_{f^3}",
            font_size=18,
        ).next_to(construction_line1, DOWN * 0.2)

        construction_line2_label = MathTex(
            r"Q_{f^1}",
            font_size=18,
        ).next_to(construction_line2, DOWN * 0.2)

        construction_line3_label = MathTex(
            r"Q_{f^2}",
            font_size=18,
        ).next_to(construction_line3, DOWN * 0.2)

        self.play(
            Create(graph),
            Create(labels),
            Create(line1),
            Write(line1_label_right),
            Create(line2),
            Write(line2_label_right),
            Create(line3),
            Write(line3_label_right),
            Create(diag_line),
            Write(diag_line_label),
            Write(line1_label_left),
            Write(line2_label_left),
            Write(line3_label_left),
            run_time=3,
        )

        self.play(
            Create(construction_line1),
            Create(construction_line2),
            Create(construction_line3),
            Write(construction_line1_label),
            Write(construction_line2_label),
            Write(construction_line3_label),
            run_time=2,
        )

        self.wait(1)


class Slide19(Scene):
    def construct(self):
        title = Tex(r"The Taylor Rule", font_size=60).shift(UP * 2.3)

        line1 = (
            Tex(
                r"""
                \begin{enumerate}
                        \item The Federal Funds rate is decided at the discretion of the FOMC (Federal Open Market Committee), and does not adhere to a strict target or monetary policy rule 
                        \item However, it roughly appears to follow a rule established by economist John Taylor, the \emph{Taylor rule}
                        \begin{enumerate}
                            \item If real GDP rises up $1\%$ above potential GDP, the Fed should raise the Federal funds rate by $\frac{1}{2}$ a percentage point
                            \item If inflation rises by $1$ percentage point above its target of $2\%$, then the Fed should raise the Federal funds rate by $\frac{1}{2}$ a percentage point
                            \item When real GDP is equal to potential GDP and inflation is equal to its target rate of $2\%$, the Federal funds rate should remain at about $4\%$, which would imply a real interest rate of $2\%$
                        \end{enumerate}
                    \end{enumerate}""",
                font_size=26,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.play(Write(title))
        self.play(Write(line1))


class Slide20(Scene):
    def construct(self):
        title = Tex(r"The Taylor Rule", font_size=60).shift(UP * 2.3)

        line1 = (
            Tex(
                r"""
                \begin{enumerate}
                        \item The Federal Funds rate is decided at the discretion of the FOMC (Federal Open Market Committee), and does not adhere to a strict target or monetary policy rule 
                        \item However, it roughly appears to follow a rule established by economist John Taylor, the \emph{Taylor rule}
                        \begin{enumerate}
                            \item If real GDP rises up $1\%$ above potential GDP, the Fed should raise the Federal funds rate by $\frac{1}{2}$ a percentage point
                            \item If inflation rises by $1$ percentage point above its target of $2\%$, then the Fed should raise the Federal funds rate by $\frac{1}{2}$ a percentage point
                            \item When real GDP is equal to potential GDP and inflation is equal to its target rate of $2\%$, the Federal funds rate should remain at about $4\%$, which would imply a real interest rate of $2\%$
                        \end{enumerate}
                    \end{enumerate}""",
                font_size=26,
            )
        ).next_to(title, DOWN, buff=0.7)

        self.add(title)
        self.add(line1)

        self.play(Unwrite(line1))

        new_title = Tex(r"The Real Taylor Rule")

        self.play(
            Transform(title, new_title, replace_mobject_with_target_in_scene=True)
        )

        self.wait(2)

        new_line1 = Tex(
            r"""The actual equation of the Taylor rule can be expressed as follows:
            \[
                i = r^* + \pi^* + a(\pi - \pi^*) + b(y - y^*)
            \]
            However, we are legally obligated to inform you that this is not necessary for entry-level Macroeconomics courses such as this one.
            """,
            font_size=26,
        )

        self.play(new_title.animate.shift(UP * 2.3))
        self.play(Write(new_line1))


class Slide21(Scene):
    def construct(self):
        new_title = Tex(r"The Real Taylor Rule").shift(UP * 2.3)

        self.add(new_title)

        new_line1 = Tex(
            r"""The actual equation of the Taylor rule can be expressed as follows:
            \[
                i = r^* + \pi^* + a(\pi - \pi^*) + b(y - y^*)
            \]
            However, we are legally obligated to inform you that this is not necessary for entry-level Macroeconomics courses such as this one.
            """,
            font_size=26,
        )

        self.add(new_line1)

        new_line2 = Tex(
            r"""
                Additionally and disappointingly, the Taylor rule shares only in name with its more famous cousin, the Taylor series. You may find the following information useful for your FRQ:
                
            """,
            font_size=26,
        ).next_to(new_title, DOWN, buff=0.7)

        new_new_title = Tex(r"The Taylor Series").shift(UP * 2.3)

        self.play(Transform(new_title, new_new_title))
        self.play(Transform(new_line1, new_line2))

        intro = Tex(
            r"Consider the function $e^x$. We can represent it as a series\\ expansion of polynomial terms as follows:",
            font_size=30,
        ).next_to(new_line2, DOWN, buff=0.7)

        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x",
        ).next_to(intro, DOWN, buff=0.5)
        equation.set_color_by_tex("x", YELLOW)

        self.play(Write(intro))
        self.play(Write(equation))


class Slide22(Scene):
    def construct(self):
        title = Tex(r"More on Monetary Policy", font_size=60).shift(UP * 2.3)

        line1 = (
            (
                Tex(
                    r"""
                    {{ Expansionary }} vs. {{ Restrictive }} monetary policies
                """,
                    font_size=26,
                )
            )
            .set_color_by_tex("Expansionary", "BLUE")
            .set_color_by_tex("Restrictive", "RED")
            .next_to(title, DOWN, buff=0.3)
        )
        line2 = (
            Tex(
                r"""
                \begin{enumerate}
                        \item Expansionary policies
                        \begin{enumerate}
                            \item Implemented when economy is experiencing recession, high unemployment, or low inflation
                            \item Fed stimulates economy by increasing money supply (hence, expansionary), $\rightarrow$~lower interest rates
                            \item Selling in open market operations, lowering reserve ratio, reducing discount rate
                        \end{enumerate}
                        \item Restrictive policies
                        \begin{enumerate}
                            \item Implemented when economy is experiencing high inflation and the Fed wants to slow growth of aggregate demand
                            \item Fed reduces money supply, increasing interest rates, $\rightarrow$~borrowing more expensive
                            \item Buying in open market operations, raising reserve ratio, increasing discount rate
                        \end{enumerate}
                    \end{enumerate}
                    
                    """,
                font_size=20,
            )
        ).next_to(line1, DOWN, buff=0.3)

        self.play(Write(title))
        self.play(Write(line1), Write(line2))


class Credits(Scene):
    def construct(self):
        title = Tex(r"Credits", font_size=60).shift(UP * 2.3)

        line1 = (
            (
                Tex(
                    r"""
                    Thank you to Youwen for doing all of the work.
                """,
                    font_size=26,
                )
            )
            .set_color_by_tex("Expansionary", "BLUE")
            .set_color_by_tex("Restrictive", "RED")
            .next_to(title, DOWN, buff=0.3)
        )

        line2 = (
            Tex(
                r"""
                Additionally, thanks to Grant Sanderson of 3Blue1Brown and the Manim Community
                    for their free and open source contributions to the Manim project, without
                        which this presentation would not have been possible.
                """,
                font_size=22,
            )
        ).next_to(line1, DOWN, buff=0.5)

        line3 = Tex(
            r"""All 1700+ lines of source code for this website and the animations can be found on Github, released under the GNU General Public License for
                        anyone to use, distribute, or hack.""",
            font_size=18,
        ).next_to(line2, DOWN, buff=0.5)

        license = Tex(
            r"""
            MIT License

Copyright (c) 2018 3Blue1Brown LLC\\

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:\\

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.\\

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.\\

\medskip

Copyright (C) 2024  Youwen Wu

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.\\

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.\\

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
""",
            font_size=6,
        ).next_to(line3, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(line1))
        self.play(Write(line2), Write(line3))
        self.play(Write(license))

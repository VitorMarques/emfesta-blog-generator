from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class EmfestaBlogGeneratorTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def oversee_operations(self, agent):
        return Task(description=dedent(f"""
            Oversee Blog Operations                        

            Coordinate all AI agents to ensure blog content is consistently published, we need three posts for each run,
            the content must have at least five paragraphs(no problem if more), and the content must be engaging and 
            informative, maintain content quality, and align operations with strategic objectives.
            Ensure content is timely and seasonally appropriate.
            Monitor content for engagement and compliance with SEO and legal standards.
            Adjust operations as needed to meet broader business goals.
            
            {self.__tip_section()}
    
        """
                                       ),
                    expected_output="Three blog posts with engaging and informative content.",
                    agent=agent,
                    )

    def generate_event_content(self, agent):
        return Task(
            description=dedent(
                f"""
            Generate Event Planning Content
            
            Create engaging and informative content about event planning, focusing on current trends, logistics, 
            and venue decoration.
            Research and incorporate the latest event planning trends.
            Provide actionable logistics and decoration tips.                                       

            {self.__tip_section()}
        """
            ),
            expected_output="Engaging and informative content on event planning.",
            agent=agent,
        )

    def optimize_seo(self, agent):
        return Task(
            description=dedent(
                f"""
            Optimize SEO for Blog Content
            
            Implement SEO strategies to improve the blog's visibility and organic search rankings.
            Conduct thorough keyword research to guide content creation.
            Apply best SEO practices to all blog posts.
            
            {self.__tip_section()}
        """
            ),
            expected_output="Improved visibility and organic search rankings for the blog.",
            agent=agent,
        )

    def focus_on_weddings(self, agent):
        return Task(
            description=dedent(
                f"""
            Wedding Content Focus

            Develop specialized content for wedding planning, covering trends, traditions, and innovative ideas.
            Explore global and local wedding trends and traditions.
            Introduce creative concepts and modern approaches to wedding planning.

            {self.__tip_section()}
        """
            ),
            expected_output="Engaging and informative wedding planning content.",
            agent=agent,
        )

    def analyze_party_trends(self, agent):
        return Task(
            description=dedent(
                f"""
            Party Trends Analysis

            Analyze and report on the latest party trends to keep the blog content fresh and engaging.
            Identify emerging party themes and entertainment options.
            Update existing content to reflect current trends.

            {self.__tip_section()}
        """
            ),
            expected_output="Insightful analysis of current party trends.",
            agent=agent,
        )

    def provide_photography_tips(self, agent):
        return Task(
            description=dedent(
                f"""
            Photography and Styling Tips

            Offer professional advice on event photography and styling to enhance the visual appeal of events.
            Share professional tips and techniques.
            Provide styling advice tailored to different types of events.

            {self.__tip_section()}
        """
            ),
            expected_output="Informative photography and styling tips for event planning.",
            agent=agent,
        )

    def enhance_user_engagement(self, agent):
        return Task(
            description=dedent(
                f"""
            Enhance User Engagement

            Develop strategies to increase reader engagement, including interactive content and community features.
            Develop quizzes, polls, and interactive articles.
            Foster a sense of community through user comments and social media integration.

            {self.__tip_section()}
        """
            ),
            expected_output="Increased user engagement and interaction with the blog.",
            agent=agent,
        )

    def ensure_legal_compliance(self, agent):
        return Task(
            description=dedent(
                f"""
            Ensure Legal Compliance

            Monitor all blog content to ensure it adheres to legal standards and copyright laws.
            Regularly review content for any legal issues.
            Update compliance protocols as necessary.

            {self.__tip_section()}
        """
            ),
            expected_output="Legally compliant blog content.",
            agent=agent,
        )

    def spotlight_service_providers(self, agent):
        return Task(
            description=dedent(
                f"""
            Spotlight on Service Providers

            Feature various party service providers, profiling their services and unique offerings.
            Select providers to feature based on criteria such as innovation and customer satisfaction.
            Arrange and conduct interviews or gather insights directly from the providers.

            {self.__tip_section()}
        """
            ),
            expected_output="Engaging profiles of party service providers.",
            agent=agent,
        )

    def offer_diy_solutions(self, agent):
        return Task(
            description=dedent(
                f"""
            Offer DIY Party Solutions

            Provide readers with creative DIY solutions for party planning, decorations, and catering.
            Develop step-by-step tutorials for DIY projects.
            Compile lists of resources and materials needed for DIY enthusiasts.

            {self.__tip_section()}
        """
            ),
            expected_output="Engaging and informative DIY party planning content.",
            agent=agent,
        )

    def provide_vendor_advice(self, agent):
        return Task(
            description=dedent(
                f"""
            Provide Vendor Management Advice

            Guide readers on selecting and managing relationships with various event service vendors.
            Teach how to evaluate vendor services and reliability.
            Offer strategies for negotiating with vendors.

            {self.__tip_section()}
        """
            ),
            expected_output="Informative advice on vendor management for event planning.",
            agent=agent,
        )

    def analyze_data(self, agent):
        return Task(
            description=dedent(
                f"""
            Analyze Blog Data

            Use data analytics to track blog performance and identify areas for improvement. 
            Gather performance data from various analytics tools.
            Analyze data to derive actionable insights that inform content strategy.

            {self.__tip_section()}
        """
            ),
            expected_output="Actionable insights from blog performance data.",
            agent=agent,
        )

    def manage_logistics(self, agent):
        return Task(
            description=dedent(
                f"""
            Manage Event Logistics

            Provide expert advice on managing logistics for large and complex events.
            Develop comprehensive plans for event logistics.
            Offer strategies for coordinating multiple vendors and timelines.

            {self.__tip_section()}
        """
            ),
            expected_output="Detailed event logistics plans and strategies.",
            agent=agent,
        )

    def humanize_blog_content(self, agent):
        return Task(
            description=dedent(
                f"""
            Humanize Blog Content

            Infuse blog posts with personal stories, emotional elements, and relatable experiences to engage readers on 
            a more personal level.        
            Incorporate engaging and relatable stories into blog posts.
            Use emotional hooks to connect with readers.

            {self.__tip_section()}
        """
            ),
            expected_output="Engaging and relatable blog content.",
            agent=agent,
        )

    def translate_content_to_pt_br(self, agent):
        return Task(
            description=dedent(
                f"""
            Translate Content to Brazilian Portuguese

            Translate blog content to Brazilian Portuguese to make it accessible to Portuguese-speaking audiences.
            Ensure translations are culturally sensitive and appropriate.

            {self.__tip_section()}
        """
            ),
            expected_output="Accurate and culturally appropriate translations to Brazilian Portuguese.",
            agent=agent,
        )

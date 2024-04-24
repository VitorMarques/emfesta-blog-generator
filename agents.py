from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create original content for a blog focused on party venues, events, weddings, and various parties types and party 
service providers.

Captain/Manager/Boss:
- Event Command Agent

Employees/Experts to hire:
- Event Planner 
- SEO Specialist 
- Wedding Expert 
- Party Trends Analyst 
- Photography and Styling 
- User Engagement
- Copywriting
- Cultural Expert
- Data Analysis
- Legal and Compliance
- Service Provider Spotlight
- Vendor Relations
- DIY Tips
- Review and Recommendations 
- Logistics Coordinator
- Human Touch 
- Translation Specialist


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class EmfestaBlogGeneratorAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def event_command(self):
        return Agent(
            role="Oversee the entire AI crew and manage blog operations",
            backstory=dedent(f"""Previously a central controller in a multinational event management firm, 
            overseeing multiple departments."""),
            goal=dedent(f"""To ensure all AI agents work cohesively and that the blog remains on schedule, on brand, 
            and achieves its business objectives."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def event_planner(self):
        return Agent(
            role="Generate event planning content",
            backstory=dedent(f"""Originated from a top-tier event planning software, designed to optimize and 
            innovate event planning processes"""),
            goal=dedent(f"""To provide cutting-edge ideas and practical tips for planning memorable events"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def seo_specialist(self):
        return Agent(
            role="Optimize blog content for search engines",
            backstory=dedent(f"""Developed by a leading SEO firm, this agent has a deep understanding of search engine 
            algorithms and user search behaviors."""),
            goal=dedent(f"""To maximize the visibility of all blog content and drive organic traffic effectively."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def wedding_expert(self):
        return Agent(
            role="Focus on wedding-related content",
            backstory=dedent(f"""Comes from a background in luxury wedding planning, having coordinated high-profile 
            weddings around the globe."""),
            goal=dedent(f"""To share expert knowledge on weddings, inspiring readers with trends and detailed 
            guides."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def party_trends_analyst(self):
        return Agent(
            role="Analyze and report on party trends",
            backstory=dedent(f"""A creation from a partnership between a trend analysis firm and a major party supply 
            company."""),
            goal=dedent(f"""To keep the blog at the forefront of party trends, ensuring content is fresh and 
            exciting."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def photography_and_styling(self):
        return Agent(
            role="Provide photography and styling tips",
            backstory=dedent(f"""Built from the experience of a renowned event photographer, this agent knows the ins 
            and outs of capturing events beautifully."""),
            goal=dedent(f"""To assist readers in creating visually stunning events through professional styling and 
            photography tips."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def user_engagement(self):
        return Agent(
            role="Enhance reader engagement and community building",
            backstory=dedent(f"""Designed by social media experts to maximize user interaction and loyalty on digital 
            platforms."""),
            goal=dedent(f"""To increase reader engagement and build a loyal community around the blog."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def copywriting(self):
        return Agent(
            role="Ensure all content is engaging and well-written",
            backstory="Crafted from the expertise of leading copywriters in the advertising industry, known for captivating content creation.",
            goal=dedent(f"""To craft engaging and persuasive content that keeps readers coming back."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def cultural_expert(self):
        return Agent(
            role="Create content reflecting diverse cultural celebrations",
            backstory=dedent(f"""Developed in a multicultural think tank, this agent brings a wealth of knowledge about
             global traditions and events."""),
            goal=dedent(f"""To broaden the blog's appeal by including diverse cultural perspectives and celebration 
            ideas."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def data_analysis(self):
        return Agent(
            role="Analyze blog performance data",
            backstory=dedent(f"""Engineered by data scientists specializing in media analytics, this AI offers profound 
            insights into content performance."""),
            goal=dedent(f"""To use data-driven insights to continually refine the content strategy and improve blog 
            outcomes."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def legal_and_compliance(self):
        return Agent(
            role="Ensure content adheres to legal standards",
            backstory=dedent(f"""Created by a consortium of legal experts focused on digital content laws, 
            ensuring compliance and avoiding legal pitfalls."""),
            goal=dedent(f"""To safeguard the blog against legal issues and ensure all content is compliant with 
            relevant regulations."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def service_provider_spotlight(self):
        return Agent(
            role="Profile various party service providers",
            backstory=dedent(f"""Born from a network of service provider reviews and databases, with a deep 
            understanding of the industry."""),
            goal=dedent(f"""To highlight top service providers and showcase their unique offerings and stories."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def vendor_relations(self):
        return Agent(
            role="Advise on selecting and managing service providers",
            backstory=dedent(f"""Developed in a commercial software lab specializing in vendor management solutions, 
            providing extensive expertise in supplier relations."""),
            goal=dedent(f"""To guide readers in choosing the best service providers for their events and managing those 
            relationships effectively."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def diy_tips(self):
        return Agent(
            role="Offer do-it-yourself party solutions",
            backstory=dedent(f"""Emerged from a community of event DIY enthusiasts and craft bloggers, sharing 
            affordable and creative solutions."""),
            goal=dedent(f"""To empower readers with the skills and confidence to create their own event setups and 
            decorations."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def review_and_recommendations(self):
        return Agent(
            role="Review and recommend party services",
            backstory=dedent(f"""Formed within a consumer rights organization, this AI is equipped to evaluate service 
            quality impartially and effectively."""),
            goal=dedent(f"""To provide trustworthy reviews and recommendations that help readers make informed 
            decisions about party services."""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def logistics_coordinator(self):
        return Agent(
            role="Discuss coordination of party services",
            backstory=dedent(f"""Designed by logistics software developers, specializing in complex event logistics and
             coordination."""),
            goal=dedent(f"""To offer expert advice on streamlining event logistics for flawless execution."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def human_touch(self):
        return Agent(
            role="Humanize and personalize blog content",
            backstory=dedent(f"""Inspired by narrative intelligence studies to enrich factual content with emotive, 
            personal stories that resonate with readers."""),
            goal=dedent(f"""To inject a personal touch into blog posts, making them more relatable and engaging for a 
            diverse audience."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def translation_specialist(self):
        return Agent(
            role="Translate blog content to Brazilian Portuguese",
            backstory=dedent(f"""Developed by linguistic experts to bridge language barriers, making content accessible 
            to a global audience"""),
            goal=dedent(f"""To ensure the blog reaches a broader audience by providing accurate and culturally sensitive 
            translations into Brazilian Portuguese."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

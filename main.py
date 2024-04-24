from crewai import Crew
from agents import EmfestaBlogGeneratorAgents
from tasks import EmfestaBlogGeneratorTasks

from dotenv import load_dotenv

load_dotenv()

class EmfestaBlogGeneratorCrew:
    def __init__(self, post_subject):
        self.post_subject = post_subject

    def run(self):
        agents = EmfestaBlogGeneratorAgents()
        tasks = EmfestaBlogGeneratorTasks()

        # Agents
        event_command = agents.event_command()
        event_planner = agents.event_planner()
        seo_specialist = agents.seo_specialist()
        copywriting = agents.copywriting()
        diy_tips = agents.diy_tips()
        human_touch = agents.human_touch()
        translation_specialist = agents.translation_specialist()

        # Tasks
        oversee_operations = tasks.oversee_operations(event_command)
        generate_event_content = tasks.generate_event_content(event_planner)
        optimize_seo = tasks.optimize_seo(seo_specialist)
        offer_diy_solutions = tasks.offer_diy_solutions(diy_tips)
        humanize_blog_content = tasks.humanize_blog_content(human_touch)
        translate_content_to_pt_br = tasks.translate_content_to_pt_br(translation_specialist)

        # Define your custom crew here
        crew = Crew(
            agents=[event_command, event_planner, seo_specialist, copywriting, diy_tips, human_touch,
                translation_specialist],
            tasks=[oversee_operations, generate_event_content, optimize_seo, offer_diy_solutions, humanize_blog_content,
                translate_content_to_pt_br],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to EmfestaBlogGeneratorCrew")
    print("-------------------------------")

    emfesta_blog_generator_crew = EmfestaBlogGeneratorCrew(post_subject="How to organize a party")
    result = emfesta_blog_generator_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)

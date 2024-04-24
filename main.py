from flask import Flask, request, jsonify
from crewai import Crew
from agents import EmfestaBlogGeneratorAgents
from tasks import EmfestaBlogGeneratorTasks

from dotenv import load_dotenv

load_dotenv()

server = Flask(__name__)

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
        #copywriting = agents.copywriting()
        diy_tips = agents.diy_tips()
        human_touch = agents.human_touch()
        translation_specialist = agents.translation_specialist()

        # Tasks
        oversee_operations = tasks.oversee_operations(event_command)
        generate_event_content = tasks.generate_event_content(event_planner)
        optimize_seo = tasks.optimize_seo(seo_specialist)
        #copywriting_task = tasks.copywriting(copywriting)
        offer_diy_solutions = tasks.offer_diy_solutions(diy_tips)
        humanize_blog_content = tasks.humanize_blog_content(human_touch)
        translate_content_to_pt_br = tasks.translate_content_to_pt_br(translation_specialist)

        # Define your custom crew here
        crew = Crew(
            agents=[event_command, event_planner, seo_specialist, diy_tips, human_touch, translation_specialist],
            tasks=[oversee_operations, generate_event_content, optimize_seo, offer_diy_solutions, 
                humanize_blog_content, translate_content_to_pt_br],
            verbose=True,
        )

        result = crew.kickoff()
        return result


@server.route('/generate-article', methods=['POST'])
def generate_article():
    data = request.json
    emfesta_blog_generator_crew = EmfestaBlogGeneratorCrew(data['post_subject'])
    result = emfesta_blog_generator_crew.run()
    return jsonify(result)

if __name__ == '__main__':
    server.run(debug=True)

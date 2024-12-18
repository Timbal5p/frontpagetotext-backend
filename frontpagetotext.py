import scratchattach as sa

session = sa.login_by_id("session_id", username="username")
cloud = session.connect_cloud("project_id")
client = cloud.requests(no_packet_loss=True)

@client.request
def ping():
    print("pong!")
    return "pong" 

@client.request
def get_frontpage_mode_1():
    frontpage_text = sa.featured_data()
    print("sending '" + str(frontpage_text) + "'")
    return str(frontpage_text)

@client.request
def get_frontpage_mode_2_step_1():
    print("sending frontpage in mode 2... (Step 1/8)")
    print("getting scratch news...")
    frontpage_news = sa.get_news(limit=10, offset=0)
    print("done, returning...")
    return str(frontpage_news)

@client.request
def get_frontpage_mode_2_step_2():
    print("sending frontpage in mode 2... (Step 2/8)")
    print("getting featured projects...")
    featured_projects = sa.featured_projects()
    print("done, returning...")
    return str(featured_projects)

@client.request
def get_frontpage_mode_2_step_3():
    print("sending frontpage in mode 2... (Step 3/8)")
    print("getting featured studios...")
    featured_studios = sa.featured_studios()
    print("done, returning...")
    return str(featured_studios)

@client.request
def get_frontpage_mode_2_step_4():
    print("sending frontpage in mode 2... (Step 4/8)")
    print("getting top loved projects...")
    loved_projects = sa.top_loved()
    print("done, returning...")
    return str(loved_projects)

@client.request
def get_frontpage_mode_2_step_5():
    print("sending frontpage in mode 2... (Step 5/8)")
    print("getting top remixed projects...")
    most_remixed_projects = sa.top_remixed()
    print("done, returning...")
    return str(most_remixed_projects)

@client.request
def get_frontpage_mode_2_step_6():
    print("sending frontpage in mode 2... (Step 6/8)")
    print("getting newest projects... (not displayed in scratchs frontpage)")
    new_projects = sa.newest_projects()
    print("done, returning...")
    return str(new_projects)

@client.request
def get_frontpage_mode_2_step_7():
    print("sending frontpage in mode 2... (Step 7/8)")
    print("getting SDS (Scratch Design Studio) projects...")
    sds_projects = sa.design_studio_projects()
    print("done, returning...")
    return str(sds_projects)

@client.request
def get_frontpage_mode_2_step_8():
    print("sending frontpage in mode 2... (Step 8/8)")
    print("getting curated projects...")
    curated_projects = sa.curated_projects()
    print("mode 2 request sucessfully finished!")
    print("done, returning...")
    return str(curated_projects)

@client.event
def on_ready():
    print("ready!")
    
@client.event
def on_error(request, e):
    print("Request: ", request.name, request.requester, request.arguments, request.timestamp, request.id)
    print("Error that occured: ", e)
    
    
client.start(thread=True)

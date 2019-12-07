#Making a bot from scratch

1) do rasa init
2) once all files are populted, we will make changes to it for our weather bot
3) change the domanin file to include our weather bot (intents, entities, slots, actions, templates)
4) in the config.yml file to provide embeddins to use and language to use.
5) make changes to actions file to include any custom actions to be made.
6) change the endpoints to specify the port to be used by rasa when running web event.
7) specify nlu i.e greeting, info, goodbye data data in nlu.md
8) write stories to begin with which we can populate further by using rasa interactive.

###Commands:

> train nlu command : rasa train nlu
> in a new tab run : rasa run actions
> train the core command: rasa train
> launch the rasa interactive to train model on the go: rasa interactive



At any time to try the model run: rasa shell

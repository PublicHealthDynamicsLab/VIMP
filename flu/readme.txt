From Mary Krauland and Lexi Mandell


influenzamodel.fred: This is the top-level model file that you use when running a FRED job from the terminal. It includes the global and personal variables that you can set for the type of flu you're modeling as Mary explained earlier. It is also where you choose to include the "accessory models" like vaccination, school breaks, or prior immunity.
flu.fred: This is the base model for flu. 
antiviral_flu.fred: This is the base model of flu with antivirals added. You would choose either this or flu.fred for a given model. The difference is that a proportion of those that are symptomatic receive antivirals that decrease hospitalization and death rates.
fluvaccine.fred: This is the base model for vaccination. You can change the proportion of the population vaccinated, the timing of vaccination, or the waning of vaccination protection here.
IMMUNITY.fred: administers a distribution of immunity from prior infection in the population and wanes that immunity
GROUP.fred: tracks infections, hospitalizations, and deaths by CDC age group
TRACK.fred: tracks combined vaccination and infection status (breakthrough infections)
WHERE.fred: tracks infections by FRED location (includes Household, Neighborhood, School, Classroom, Workplace, Office, and external)
breaks.fred: This model closes schools for winter, spring, and summer breaks. The dates can be adjusted. 

Transmissibility is currently set to 0.75 which as Mary mentioned is what we usually use for an H3N2-type influenza. There are links in the model files themselves to sources for data that I used to parameterize such as vaccination, hospitalization, or death rates. Let me know if you have any questions or have trouble accessing the files!

Ben,

I would recommend not using the antiviral model, Lexi developed it but we haven’t published anything with it or done a lot of calibration and I think it is an unnecessary complication for you.

The GROUP, TRACK, and WHERE models are just used for tracking purposes and you can use whichever are useful for you. For example, the WHERE model tracks in which mixing group infection takes place, so if you don’t care about that then you can leave it out. If you have any questions about what a model is used for or how a model works, please ask. I think most of them are pretty self-explanatory.

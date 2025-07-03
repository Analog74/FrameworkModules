
-- quest configuration + function to get quest from id

local Module = {}

Module.Quests = {
	{
		ID = '_appleCollectQuest',
		
		Contributors = { 'onCollect_Apple' },
		RequiredContributions = 3,
		
		Reward = function(LocalPlayer, playerProfile)
			playerProfile.Data.Cash += 300
			playerProfile.Data.Gems += 5
		end,
		
		Display = {
			Title = {
				Text = 'Apple Collector',
				TextColor3 = Color3.new(0.921569, 0.105882, 0.121569),
			},
			
			Description = {
				Text = 'Collect some apples to complete this quest!',
				TextColor3 = Color3.new(1, 1, 1),
			},
		},
	},
	{
		ID = '_pearCollectQuest',

		Contributors = { 'onCollect_Pear' },
		RequiredContributions = 3,

		Reward = function(LocalPlayer, playerProfile)
			playerProfile.Data.Cash += 250
			playerProfile.Data.Gems += 3
		end,

		Display = {
			Title = {
				Text = 'Pear Collector',
				TextColor3 = Color3.new(0.643137, 0.866667, 0.286275),
			},

			Description = {
				Text = 'Collect some pears to complete this quest!',
				TextColor3 = Color3.new(1, 1, 1),
			},
		},
	},
}

function Module:GetQuestFromID(questID)
	for index, questData in ipairs( Module.Quests ) do
		if questData.ID == questID then
			return questData
		end
	end
	return nil
end

return Module

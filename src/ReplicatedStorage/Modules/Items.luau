
local Module = {}

Module.Items = {
	{
		ID = 'Apple',

		Model = 'AppleMesh',
		Icon = false,
		Viewport = {
			Model = CFrame.new(),
			Camera = CFrame.new( Vector3.new(1.25, 1, 0), Vector3.new() )
		},

		Display = {
			Title = {
				Text = 'Apple',
				TextColor3 = Color3.new(0.937255, 0.172549, 0.184314),
			},
		},
	},

	------------- / / Next Item // -----------	
	{
		ID = 'Pear',

		Model = 'PearMesh',
		Icon = false,
		Viewport = {
			Model = CFrame.new(),
			Camera = CFrame.new( Vector3.new(1.25, 1, 0), Vector3.new() )
		},

		Display = {
			Title = {
				Text = 'Pear',
				TextColor3 = Color3.new(0.611765, 0.819608, 0.301961),
			},
		},
	},
	------------- / / Next Item // -----------	
	{
		ID = 'FruitSalad',

		Model = 'DancePotion',
		Icon = false,
		Viewport = {
			Model = CFrame.new(),
			Camera = CFrame.new( Vector3.new(1.25, 1, 0), Vector3.new() )
		},

		Display = {
			Title = {
				Text = 'Potion2',
				TextColor3 = Color3.new(0.24, 0.82, 0.26),
			},
		},
	},

	------------- / / Next Item // -----------	
	{
		ID = 'Banana',

		Model = 'Banana',
		Icon = false,
		Viewport = {
			Model = CFrame.new(),
			Camera = CFrame.new( Vector3.new(1.25, 1, 0), Vector3.new() )
		},

		Display = {
			Title = {
				Text = 'Banana',
				TextColor3 = Color3.new(0.24, 0.82, 0.26),
			},
		},
	},

	------------- / / Next Item // -----------	
	{
		ID = 'Potion',

		Model = 'PotionMesh',
		Icon = false,
		Viewport = {
			Model = CFrame.new(),
			Camera = CFrame.new( Vector3.new(1.25, 1, 0), Vector3.new() )
		},

		Display = {
			Title = {
				Text = 'Potion',
				TextColor3 = Color3.new(0.24, 0.82, 0.26),
			},
		},
	},

}

function Module:GetItemFromID(itemID)
	for index, itemData in ipairs( Module.Items ) do
		if itemData.ID == itemID then
			return itemData
		end
	end
	return nil
end

return Module

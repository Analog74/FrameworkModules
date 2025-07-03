
local Module = { }

Module.Crafting = {
	{
		ID = 'FruitSalad', -- The craftable item
		Quantity = 1,
		Materials = {
			Pear = 2,
			Apple = 2,
		},
	},

	{
		ID = 'Potion', -- The craftable item
		Quantity = 1,
		Materials = {
			Pear = 2,
			Apple = 2,
		},
	},

}

function Module:GetCraftableFromID( craftableID )
	for index, craftMatrix in ipairs( Module.Crafting ) do
		if craftMatrix.ID == craftableID then
			return craftMatrix, index
		end
	end
	return nil, nil
end

function Module:CanCraftCraftable( inventoryTable, craftableID )
	local craftableConfig = Module:GetCraftableFromID( craftableID )
	if not craftableConfig then
		return false
	end
	for materialName, materialCount in pairs( craftableConfig.Materials ) do
		if (not inventoryTable[materialName]) or (inventoryTable[materialName] < materialCount) then
			return false
		end
	end
	return true
end

return Module


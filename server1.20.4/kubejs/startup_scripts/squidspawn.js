onEvent('worldgen.add', e =>{
    e.addSpawn(spawn => {
        spawn.category = 'water_creature'
        spawn.entity = 'minecraft:squid'
        spawn.weight = 90
        spawn.minCount = 4
        spawn.maxCount = 4
    })
})

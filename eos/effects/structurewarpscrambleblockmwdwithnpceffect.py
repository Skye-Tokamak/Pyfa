# Not used by any item
from eos.saveddata.module import State

# Not used by any item
runTime = "early"
type = "projected", "active"


def handler(fit, module, context):
    if "projected" in context:
        fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))
        if module.charge is not None and module.charge.ID == 47336:
            for mod in fit.modules:
                if not mod.isEmpty and mod.state > State.ONLINE and (
                        mod.item.requiresSkill("High Speed Maneuvering")
                        or mod.item.requiresSkill("Micro Jump Drive Operation")
                ):
                    mod.state = State.ONLINE

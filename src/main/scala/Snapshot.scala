import scala.collection.mutable.ListBuffer

class Snapshot {
  var position = new ListBuffer[(Int, Int)]
  var snapshotNum = new ListBuffer[Int]

  def billboardShot(movement: Movement) {
    val billboardCoordinate = (movement.x, movement.y)
    if (position contains billboardCoordinate) {
      val billboardIndex = position.indexOf(billboardCoordinate)
      snapshotNum(billboardIndex) = snapshotNum(billboardIndex) + 1
    } else {

      position += billboardCoordinate
      snapshotNum += 1
    }

  }

  def uniqueBillboardNum(): Int = {
    val billboardNum = position.length
    return billboardNum
  }
}

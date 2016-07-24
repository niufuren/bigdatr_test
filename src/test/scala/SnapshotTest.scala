import org.scalatest._
import scala.collection.mutable.ListBuffer

class SnapshotSpec extends FlatSpec {

  def fixture =
    new {
      val snapshot = new Snapshot
      val movement = new Movement
      movement.x = 1
      movement.y = 1
    }

  "A snapshot class" should "record the position and counts of a potographed billboard" in {
    val f = fixture
    f.snapshot.billboardShot(f.movement)
    assert(f.snapshot.position === ListBuffer((1, 1)))
    assert(f.snapshot.snapshotNum === ListBuffer(1))

    f.snapshot.billboardShot(f.movement)
    assert(f.snapshot.snapshotNum === ListBuffer(2))

  }

  it should "count the number of unique billboards" in {
    val f = fixture
    assert(f.snapshot.uniqueBillboardNum() === 0)

    f.snapshot.billboardShot(f.movement)
    assert(f.snapshot.uniqueBillboardNum() === 1)

    f.snapshot.billboardShot(f.movement)
    assert(f.snapshot.uniqueBillboardNum() === 1)
  }

}

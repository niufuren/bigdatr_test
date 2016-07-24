import org.scalatest._
import scala.collection.mutable.ListBuffer

class DroneSpec extends FlatSpec {

  def fixture =
    new {
      val drone = new Drone
    }

  "A drone class" should "be able to process the moving up instructor '^'" in {
    val f = fixture
    f.drone.process('^')
    assert(f.drone.movement.x === 0)
    assert(f.drone.movement.y === 1)

  }

  it should "be able to process the moving down instructor 'v'" in {
    val f = fixture
    f.drone.process('v')
    assert(f.drone.movement.x === 0)
    assert(f.drone.movement.y === -1)
  }

  it should "be able to process the moving left instructor '<'" in {
    val f = fixture
    f.drone.process('<')
    assert(f.drone.movement.x === -1)
    assert(f.drone.movement.y === 0)
  }

  it should "be able to process the moving right instructor '>'" in {
    val f = fixture
    f.drone.process('>')
    assert(f.drone.movement.x === 1)
    assert(f.drone.movement.y === 0)
  }

  it should "be able to process the snapshot instructor 'x'" in {
    val f = fixture
    f.drone.process('x')
    assert(f.drone.snapshot.position === ListBuffer((0,0)))
    assert(f.drone.snapshot.snapshotNum === ListBuffer(1))
  }
  
  it should "be able to know the position of the drone" in{
    val f = fixture
    assert(f.drone.getCoordinate === (0,0))
    f.drone.process('>')
    assert(f.drone.getCoordinate === (1,0))

  }

}

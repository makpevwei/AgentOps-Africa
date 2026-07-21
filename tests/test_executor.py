from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.executor import Executor
from agentops.domains.agents.task import AgentTask, TaskStatus
from agentops.domains.agents.task_result import TaskResult


class FakeAgent:
    def execute(self, task, context):
        return TaskResult(
            success=True,
            provider="FakeAgent",
            output={"message": "ok"},
        )


class FakeRegistry:
    def get(self, service):
        return FakeAgent()


def test_executor_executes_task():
    executor = Executor()

    # Replace the real registry
    executor.registry = FakeRegistry()

    plan = ExecutionPlan(goal="Test Execution")

    plan.add_task(
        AgentTask(
            id=1,
            name="Test Task",
            service="research",
            action="company_profile",
            description="Test",
            payload={},
            depends_on=[],
        )
    )

    context = executor.execute(plan)

    assert context.successful is True
    assert context.completed_tasks == [1]

    task = plan.tasks[0]

    assert task.status == TaskStatus.COMPLETED
    assert task.is_complete is True
    assert task.is_failed is False

    assert task.result is not None
    assert task.result.success is True
    assert task.result.provider == "FakeAgent"
    assert task.result.output == {"message": "ok"}